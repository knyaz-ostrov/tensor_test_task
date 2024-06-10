"""
Модуль содержит в себе фикстуры для тестирования сценариев.
"""
import pytest

from selenium import webdriver

from chrome_options import ChromeOptions


@pytest.fixture(scope='session')
def browser():
    """
    Фикстура для инициализации WebDriver браузера
    перед выполнением тестов и завершения работы после их завершения.

    :return: Возвращает объект WebDriver для работы с браузером.
    """
    driver = webdriver.Chrome(options=ChromeOptions.chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()
