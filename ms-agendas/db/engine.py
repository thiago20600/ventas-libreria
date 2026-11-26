from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine
from ..config.env_config import settings

DATABASE_URL = settings.db_url

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


DbSession = Annotated[Session, Depends(get_db)]