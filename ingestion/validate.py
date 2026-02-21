# type: ignore[index]
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO)


def validate_data(df: pd.DataFrame) -> None:
    logging.info("Validating dataset")

    if df.empty:
        raise ValueError("Dataset is empty")

    if df["geo_code"].isnull().any():
        raise ValueError("Null values detected in geo_code")

    if df["year"].isnull().any():
        raise ValueError("Null values detected in year")

    if df["gdp_mio_eur"].isnull().any():
        raise ValueError("Null values detected in gdp_mio_eur")

    if (df["gdp_mio_eur"] < 0).any():
        raise ValueError("Negative GDP values detected")

    duplicates = df.duplicated(subset=["geo_code", "year"]).sum()
    if duplicates > 0:
        raise ValueError(f"Duplicate rows detected: {duplicates}")

    logging.info("Validation passed successfully")
