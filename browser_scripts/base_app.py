"""
Базовый модуль для работы с selenium
и совершения действий на веб-страницах.
"""
from typing import Tuple, List
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait, WebElement


class BasePage:
    """
    Класс содержащий методы для работы
    с selenium.
    """
    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver

    def go_to_site(self, url: str) -> None:
        """
        Переходит на указанный веб-сайт.

        :param url: Ссылка на сайт.
        :return:
        """
        self.driver.get(url)

    def find_element(self, locator: Tuple[str, str], time: int = 10) -> WebElement:
        """
        Ожидает появление элемента на веб-странице
        в течение определенного времени и скроллит
        к нему, чтобы он оказался активной области
        окна браузера.

        :param locator: Локатор элемента, по которому
                        будет осуществляться поиск элемента.
        :param time: Время ожидания в секундах (по умолчанию 10 секунд).
        :return: Возвращает найденный элемент, если он появился в течение указанного времени.
                 В противном случае вызывается исключение TimeoutException.
        """
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не найден элемент {locator}"
        )
        self.__scroll_to_element(element)

        return element

    def find_elements(self, locator: Tuple[str, str], time: int = 10) -> List[WebElement]:
        """
        Ожидает появление элементов на веб-странице
        в течение определенного времени.

        :param locator: Локатор элементов, по которому
                        будет осуществляться поиск элементов.
        :param time: Время ожидания в секундах (по умолчанию 10 секунд).
        :return: Возвращает найденные элементы, если они появились в течение указанного времени.
                 В противном случае вызывается исключение TimeoutException.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не найден элемент {locator}"
        )

    def wait_element_by_text(self, locator, text, time=10) -> bool:
        """
        Ожидает появление элемента на веб-странице c заданным текстом
        в течение определенного времени.

        :param locator: Локатор элемента, по которому
                        будет осуществляться поиск элемента.
        :param text: Текст элемента, который нужно дождаться
        :param time: Время ожидания в секундах (по умолчанию 10 секунд).
        :return: Возвращает True, если текст найден.
        """
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Не найден элемент {locator}"
        )

    def switch_tab(self, num: int) -> None:
        """
        Переключается на указанную вкладку браузера.

        :param num: Индекс вкладки, на которую нужно переключиться (начиная с 0).
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[num])

    def __scroll_to_element(self, element: WebElement) -> None:
        """
        Прокручивает страницу так, чтобы указанный элемент был виден в видимой области браузера.

        :param element: Элемент, к которому нужно прокрутить страницу.
        :return:
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
