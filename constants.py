"""
Модуль хранит в себе константы для поиска элементов и прочее
"""
from selenium.webdriver.common.by import By


CONTACT_BUTTON = (By.LINK_TEXT, 'Контакты')
TENSOR_LOGO_BUTTON = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor.mb-12')
TENSOR_BUNNER = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
ABOUT_BUTTON = (By.CSS_SELECTOR, 'a.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
PHOTO_BLOG = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[*]/a/div[1]/img')
REGION = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
PARTNER_BLOCK_REGION = (By.XPATH, '//*[@id="city-id-2"]')
KAMCHATKA_REGION = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
DOWNLOAD_LOCAL_VERSIONS_LINK = (By.LINK_TEXT, 'Скачать локальные версии')
SBIS_PLUGIN = (By.XPATH, '//div[@data-id="plugin"]')
DOWNLOAD_PLUGIN = (By.PARTIAL_LINK_TEXT, 'Скачать (Exe')

FILE_NAME_PLUGIN = 'sbisplugin-setup-web.exe'
URL_SBIS = 'https://sbis.ru/'
