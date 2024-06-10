"""
Модуль содержит вспомогательные функции для тестов
"""
import os
import time


def check_download_file(file_path: str, timeout: int = 10) -> bool:
    """
    Метод проверяет существование файла

    :param file_path: Путь к файлу
    :param timeout: Максимальное время ожидания (В секундах)
    :return: True, если файл был найден за отведённое время
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(file_path):
            return True

    return False
