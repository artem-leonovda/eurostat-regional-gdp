import logging
import time
from typing import Dict, Any

import requests
import pandas as pd
from sqlalchemy.engine import Engine

from db_engine import get_engine
from transform import transform_data
from validate import validate_data
from load import load_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

EUROSTAT_URL: str = (
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_2gdp"
)

PARAMS: Dict[str, str] = {
    "unit": "MIO_EUR",
    "format": "JSON",
}

START_YEAR: int = 2015
END_YEAR: int = 2023


def wait_for_db(engine: Engine, retries: int = 10, delay: int = 3) -> None:
    for attempt in range(retries):
        try:
            with engine.connect():
                logging.info("Database connection established")
                return
        except Exception as e:
            logging.warning(
                f"Database not ready (attempt {attempt + 1}/{retries})"
            )
            time.sleep(delay)

    raise RuntimeError("Database connection failed after retries")


def fetch_data() -> Dict[str, Any]:
    logging.info("Fetching Eurostat data")

    response = requests.get(
        EUROSTAT_URL,
        params=PARAMS,
        timeout=60,
    )

    response.raise_for_status()
    data: Dict[str, Any] = response.json()

    if "value" not in data:
        raise ValueError("Invalid Eurostat response: 'value' field missing")

    if len(data["value"]) < 100:
        raise ValueError("Data size unexpectedly small")

    logging.info(f"Fetched {len(data['value'])} records")

    return data


def main() -> None:
    engine: Engine = get_engine()

    wait_for_db(engine)

    raw_data = fetch_data()

    df: pd.DataFrame = transform_data(
        raw_data,
        START_YEAR,
        END_YEAR,
    )

    validate_data(df)

    load_data(df, engine)

    logging.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    main()