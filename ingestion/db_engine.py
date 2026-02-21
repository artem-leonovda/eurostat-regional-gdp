from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from pathlib import Path

load_dotenv()


def running_in_docker() -> bool:
    return Path("/.dockerenv").exists()


def get_engine():
    if running_in_docker():
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
    else:
        host = os.getenv("POSTGRES_HOST_LOCAL")
        port = os.getenv("POSTGRES_PORT_LOCAL")

    url = (
        f"postgresql+psycopg2://"
        f"{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{host}:{port}/"
        f"{os.getenv('POSTGRES_DB')}"
    )

    return create_engine(url)