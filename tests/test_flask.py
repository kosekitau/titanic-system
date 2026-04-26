import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.app import app
from src.models import Person
from src.database import engine, Base, db_session


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def rollback_session():
    engine = create_engine(os.environ["DATABASE_URL"])
    session = Session(bind=engine)
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def all_drop_client():
    Base.metadata.create_all(bind=engine)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
    db_session.remove()
    Base.metadata.drop_all(bind=engine)


class Test_Flask:
    def test_print(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert response.data.decode("utf-8") == "Hello World"

    def test_jinja_render(self, client):
        response = client.get("/hello")
        html_content = response.data.decode("utf-8")
        assert "Hello Jinja2" in html_content
        assert "<h1>" in html_content

    def test_resister_data_to_DB(self, all_drop_client):
        response = all_drop_client.post(
            "/registration",
            data={
                "pclass": 1,
                "sex": "male",
                "age": 20,
                "slibSp": 1,
                "parch": 1,
                "ticket": "113803",
                "fare": 7.25,
                "cabin": "G6",
                "embarked": "S",
            },
            follow_redirects=True,
        )
        assert "Registration Successful" in response.data.decode("utf-8")
        result = db_session.query(Person).first()
        assert result.ticket == "113803"
