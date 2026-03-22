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
        assert "Hello Jinja2" in html_content
        assert "<h1>" in html_content

    def test_register_data(self, client):
        response = client.post(
            "/registeration",
            data={
                "id": 1,
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
        assert response.data.decode("utf-8") == "Registration Successful"
