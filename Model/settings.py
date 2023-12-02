from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


def create_db_and_tables_settings():
    engine = create_engine("mysql+pymysql://root:devpass@localhost:3307/tg_wawision", echo=True)
    SQLModel.metadata.create_all(engine)


class py_settings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    parent: int

