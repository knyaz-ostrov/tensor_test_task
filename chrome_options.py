"""
Модуль для хранения настроек драйвера Chrome.
"""
import os

from selenium.webdriver.chrome.options import Options


class ChromeOptions:
    """
    Класс хранит настройки для WebDriver Chrome.
    """
    chrome_options = Options()

    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://sbis.ru")

    __download_path = os.path.dirname(os.path.abspath(__file__))

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": __download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        }
    )
