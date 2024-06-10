"""
Модуль для запуска тестовых сценариев.
"""
from selenium import webdriver

from tests.scenarios import test_scenario_one, test_scenario_two, test_scenario_three

def main(browser: webdriver.Chrome) -> None:
    """
    Запускает сценарии.
    """
    test_scenario_one(browser)
    test_scenario_two(browser)
    test_scenario_three(browser)
