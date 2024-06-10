"""
Модуль для проверки сценариев тестового задания
"""
import os
import time

from selenium import webdriver
from site_pages import SiteHelper
from helpers import check_download_file
from constants import (
    CONTACT_BUTTON,
    TENSOR_LOGO_BUTTON,
    TENSOR_BUNNER,
    ABOUT_BUTTON,
    PHOTO_BLOG,
    REGION,
    PARTNER_BLOCK_REGION,
    KAMCHATKA_REGION,
    DOWNLOAD_LOCAL_VERSIONS_LINK,
    SBIS_PLUGIN,
    DOWNLOAD_PLUGIN,
    FILE_NAME_PLUGIN,
    URL_SBIS
)


def test_scenario_one(browser: webdriver.Chrome) -> None:
    """
    Проверяет переходы по нажатию кнопок,
    наличие блоков, разделов, соответствие
    ссылок и ширину и высоту фотографий

    :param browser: Объект браузера
    :return:
    """
    page = SiteHelper(browser)

    page.go_to_site(URL_SBIS)

    page.click_on_button(CONTACT_BUTTON)

    page.click_on_button(TENSOR_LOGO_BUTTON)
    page.switch_tab(1)

    assert page.find_element(TENSOR_BUNNER).text == 'Сила в людях', 'Текст баннера не совпадает'

    page.scroll_and_click_on_button(ABOUT_BUTTON)
    assert browser.current_url == 'https://tensor.ru/about', 'Ссылки не совпадают'

    photo_sizes = page.get_photo_sizes(PHOTO_BLOG)
    for i, ph in enumerate(photo_sizes, 0):
        if i == len(photo_sizes) - 1:
            break
        assert ph == photo_sizes[i+1], 'Размер фотографий не совпадает'


def test_scenario_two(browser: webdriver.Chrome) -> None:
    """
    Проверяет переходы по нажатию кнопок,
    соответствие региона, корректную смену
    региона с обновлением всей информации
    с учетом смены региона

    :param browser: Объект браузер
    :return:
    """
    page = SiteHelper(browser)

    page.go_to_site(URL_SBIS)

    page.click_on_button(CONTACT_BUTTON)

    assert page.find_element(REGION).text == 'Тюменская обл.', 'Регион определился неправильно'

    page.click_on_button(REGION)
    page.click_on_button(KAMCHATKA_REGION)

    assert page.find_element_by_text(REGION, "Камчатский край"), 'Регион был выбран неправильно'

    assert page.find_element_by_text(PARTNER_BLOCK_REGION, "Петропавловск-Камчатский"),\
        'Список партнеров не обновился'

    assert '41-kamchatskij-kraj' in browser.current_url,\
        'URL не содержит информации о выбранном регионе'
    assert 'Камчатский край' in browser.title, 'Title не содержит информации о выбранном регионе'


def test_scenario_three(browser: webdriver.Chrome) -> None:
    """
    Проверяет скачивание файла и сравнивает размер
    скачанного файла с тем, что указан на сайте

    :param browser: Объект браузер
    :return:
    """
    page = SiteHelper(browser)

    page.go_to_site(URL_SBIS)

    page.scroll_and_click_on_button(DOWNLOAD_LOCAL_VERSIONS_LINK)
    time.sleep(2)

    page.click_on_button(SBIS_PLUGIN)

    file_size_link = float(page.find_element(DOWNLOAD_PLUGIN).text.split()[-2])
    page.click_on_button(DOWNLOAD_PLUGIN)

    downloaded_file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(downloaded_file_path, FILE_NAME_PLUGIN)

    exist_file = check_download_file(file_path)

    assert exist_file, 'Файл не был скачан'
    downloaded_file_size = os.path.getsize(file_path)

    assert file_size_link == round(downloaded_file_size / (1024*1024), 2),\
                            'Фактический размер файла не совпадает с указанным'
    os.remove(file_path)
