import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    """
    Фикстура для инициализации WebDriver браузера
    перед выполнением тестов и завершения работы после их завершения.

    :return: Возвращает объект WebDriver для работы с браузером.
    """
    chrome_options = Options()
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument(
        "--unsafely-treat-insecure-origin-as-secure=https://sbis.ru"
    )
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": os.path.dirname(os.path.abspath(__file__)),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        }
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
