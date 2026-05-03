import pytest


@pytest.fixture
def dummy_data():
    return {
        "pclass": 1,
        "sex": "male",
        "age": 20,
        "slibSp": 1,
        "parch": 1,
        "ticket": "113803",
        "fare": 7.25,
        "cabin": "G6",
        "embarked": "S",
    }
