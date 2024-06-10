"""
Модуль содержит в себе фикстуры для тестирования сценариев.
"""
import shutil

import pytest
from selenium import webdriver

from constants import DOWNLOAD_PATH
from webdriver_options import ChromeOptions


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


@pytest.fixture(scope="session", autouse=True)
def cleanup_downloads(request):
    """
    Фикстура для удаления папки downloads перед и после
    выполнения тестовых сценариев.
    """
    def fin():
        """
        Удаление папки со скачанными файлами.
        """
        shutil.rmtree(DOWNLOAD_PATH)

    request.addfinalizer(fin)
