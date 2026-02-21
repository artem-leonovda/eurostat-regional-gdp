import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy import text
import logging

logging.basicConfig(level=logging.INFO)


def load_data(df: pd.DataFrame, engine: Engine) -> None:
    logging.info("Loading data into PostgreSQL")

    with engine.begin() as conn:
        conn.execute(text("DELETE FROM regional_gdp"))
        df.to_sql(
            "regional_gdp",
            conn,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=5000
        )

    logging.info("Data successfully loaded")
