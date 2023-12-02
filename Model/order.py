import datetime as dt
from pydantic import condecimal
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


def create_db_and_tables_orders():
    engine = create_engine("mysql+pymysql://root:devpass@localhost:3307/tg_wawision", echo=True)
    SQLModel.metadata.create_all(engine)


class py_orders(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    document_no: str = Field(nullable=False)
    transaction_no: int = Field(nullable=False)
    created_at: dt.datetime = Field(default_factory=dt.datetime.utcnow, nullable=False)
    total: condecimal(max_digits=10, decimal_places=3) = Field(default=0)
    name: str= Field(nullable=False)

