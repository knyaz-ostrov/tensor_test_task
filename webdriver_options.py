"""
Модуль для хранения настроек webdriver.
"""
from selenium.webdriver.chrome.options import Options

from constants import DOWNLOAD_PATH


class ChromeOptions:
    """
    Класс хранит настройки для WebDriver Chrome.
    """
    chrome_options = Options()

    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://sbis.ru")

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_PATH,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        }
    )
