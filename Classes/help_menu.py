from sqlalchemy import delete

from Services.message_service import messageService
from Repository.order_repository import orderRepository
from Model.order import py_orders
from sqlmodel import SQLModel, Session, select
from Helper.database_class import engine


def import_orders():
    delete_order_by_document_no()
    session = Session(engine)
    rows = orderRepository.get_all_data("auftrag")
    for row in rows:
        order = py_orders(document_no=row['belegnr'], transaction_no=row['internet'], created_at=row['datum'],
                          total=row['gesamtsumme'], name=row['name'])
        session.add(order)

    session.commit()


def delete_order_by_document_no():
    with Session(engine) as session:
        statement = delete(py_orders)
        result = session.exec(statement)
        session.commit()
        print(result.rowcount)

