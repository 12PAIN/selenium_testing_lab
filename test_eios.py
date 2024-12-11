import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Настройка undetected-chromedriver для использования обычного Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")


@pytest.fixture
def setup_driver():
    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()

def test_eios_login(setup_driver):
    """
    Тест для входа на сайт eios.kemsu.ru с использованием логина и пароля
    """
    driver = setup_driver
    wait = WebDriverWait(driver, 40)  # Установка явного ожидания

    # Переход на сайт eios.kemsu.ru
    driver.get("https://eios.kemsu.ru/a/eios")

    # Ожидание появления поля для ввода логина
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_input.send_keys(config.USERNAME)  # Замените на реальный логин

    # Ожидание появления поля для ввода пароля
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_input.send_keys(config.PASSWORD)  # Замените на реальный пароль

    # Нажатие на кнопку "Войти"
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'css-h0m9oy')]")))
    login_button.click()

    # Ожидание и переход в профиль
    profile_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'css-10pdxt6') and @href='/a/eios/profile']")))
    profile_link.click()

    # Ожидание появления элемента с ФИО
    fio_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[label[text()='ФИО']]/input[@readonly]")))
    fio_value = fio_input.get_attribute("value")

    # Проверка, что ФИО соответствует ожидаемому значению
    assert fio_value == config.FIO, f"Ошибка: Ожидалось '{config.FIO}', но получено '{fio_value}'"
