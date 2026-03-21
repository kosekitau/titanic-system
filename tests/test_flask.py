import pytest

from src.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class Test_Flask:
    def test_print(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert response.data.decode("utf-8") == "Hello World"

    def test_jinja_render(self, client):
        response = client.get("/hello")
        html_content = response.data.decode("utf-8")
        assert html_content == "Hello Jinja2"
        assert "<h1>" in html_content
