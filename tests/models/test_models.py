import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models import Person


@pytest.fixture
def rollback_session():
    # connection = create_engine(os.environ["DATABASE_URL"]).connect()
    # transaction = connection.begin()
    # session = Session(bind=transaction)
    engine = create_engine(os.environ["DATABASE_URL"])
    session = Session(bind=engine)
    yield session
    session.rollback()
    session.close()
    # ロールバックして入れたデータを消し去る
    # transaction.rollback()
    # connection.close()


class Test_DB:
    def test_input_data(self, rollback_session):
        person = Person(
            id=1, pclass=1, sex="male", age=20, slibSp=1, parch=1, ticket="113803", fare=7.25, cabin="G6", embarked="S"
        )
        rollback_session.add(person)
        rollback_session.flush()
        result = rollback_session.query(Person).first()
        assert result.age == 20
