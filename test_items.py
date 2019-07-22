from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_basket(browser):
    browser.get(link)
    # ожидаем загрузку страницы и кнопки, одновременно проверяем что кнопка есть
    button = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-add-to-basket')))