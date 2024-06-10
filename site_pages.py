"""
Модуль для работы с веб-страницами
"""
from typing import Tuple, List

from base_app import BasePage


class SiteHelper(BasePage):
    """
    Класс для упрощенной работы со страницами сайта.
    """
    def click_on_button(self, locator: Tuple[str, str]) -> None:
        """
        Метод кликает на кнопку.
        Если клик не удается сделать обычным способом,
        метод пытается сделать это с помощью JavaScript.

        :param locator: Кортеж (Локатор, Искомое значение)
        :return:
        """
        button = self.find_element(locator)
        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)

    def scroll_and_click_on_button(self, locator: Tuple[str, str]) -> None:
        """
        Прокручивает страницу к элементу,
        затем выполняет клик по указанной кнопке.
        Если клик не удается сделать обычным способом,
        метод пытается сделать это с помощью JavaScript

        :param locator: Кортеж (Локатор, Искомое значение)
        :return:
        """
        button = self.find_element(locator)
        self.scroll_to_element(button)
        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)

    def get_photo_sizes(self, locator: Tuple[str, str]) -> List[List[str | None]]:
        """
        Получает размеры изображений из блока фотографий на веб-странице.

        :param locator: Кортеж (Локатор, Искомое значение)
        :return: Возвращает список списков размеров изображений.
                 Каждый внутренний список содержит ширину и высоту изображения.
                 Если размеры недоступны, то вместо значения будет указано None.
        """
        photos = self.find_elements(locator, time=5)
        sizes = [[photo.get_attribute('width'), photo.get_attribute('height')] for photo in photos]
        return sizes
