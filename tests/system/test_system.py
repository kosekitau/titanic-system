import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def driver():
    selenium_driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=webdriver.ChromeOptions(),
    )
    yield selenium_driver
    selenium_driver.quit()


class Test_selenium:
    def test_hello(self, driver):
        url = "http://app:8501"
        driver.get(url)
        assert driver.current_url == url
        page_h1_title = driver.find_element(by=By.TAG_NAME, value="h1").text
        assert "Hello Jinja2" in page_h1_title
