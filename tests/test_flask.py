import pytest

from src import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class Test_Flask:
    def test_print(self):
        response = client.get("/")
        assert response.status.code == 200
        assert response.data.decode("utf-8") == "Hello World"
