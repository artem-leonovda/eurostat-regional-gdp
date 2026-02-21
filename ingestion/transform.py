from typing import Dict, Any
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def transform_data(data: Dict[str, Any], start_year: int, end_year: int) -> pd.DataFrame:
    logging.info("Transforming data")
    dim_order = data["id"]
    size_list = data["size"]
    dimensions = data["dimension"]

    dim_values = {
        dim: list(dimensions[dim]["category"]["index"].keys())
        for dim in dim_order
    }

    rows = []

    for idx_str, value in data["value"].items():
        idx = int(idx_str)
        coords = {}
        idx_tmp = idx
        for dim, dim_size in zip(reversed(dim_order), reversed(size_list)):
            coords[dim] = dim_values[dim][idx_tmp % dim_size]
            idx_tmp //= dim_size

        year = int(coords.get("time"))

        if start_year <= year <= end_year:
            rows.append({
                "geo_code": coords.get("geo"),
                "year": year,
                "gdp_mio_eur": float(value)
            })

    df = pd.DataFrame(rows)
    logging.info(f"Transformed rows: {len(df)}")
    return df
