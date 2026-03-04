import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_button_exists(browser):
    """
    Тест проверяет наличие кнопки добавления в корзину на странице товара
    """
    # Используем рабочий сайт saucedemo.com
    link = "https://www.saucedemo.com/inventory.html"
    
    print(f"\n🔍 Открываем страницу: {link}")
    browser.get(link)
    
    # Авторизуемся сначала (так как страница товаров требует авторизации)
    print("🔑 Выполняем вход в систему...")
    
    # Заполняем форму логина
    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
    )
    username_field.send_keys("standard_user")
    
    password_field = browser.find_element(By.CSS_SELECTOR, "#password")
    password_field.send_keys("secret_sauce")
    
    login_button = browser.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()
    
    # Ждем загрузки страницы с товарами
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list"))
    )
    
    print("✅ Успешный вход на страницу товаров")
    
    # Небольшая пауза для стабильности
    time.sleep(2)
    
    # Проверяем наличие кнопки добавления в корзину для первого товара
    print("🔍 Ищем кнопку добавления в корзину...")
    
    # Селекторы для кнопки добавления в корзину на saucedemo.com
    add_to_cart_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_inventory"))
    )
    
    # Проверяем, что кнопка видима и активна
    assert add_to_cart_button.is_displayed(), "❌ Кнопка не отображается на странице"
    assert add_to_cart_button.is_enabled(), "❌ Кнопка неактивна"
    
    # Получаем текст кнопки
    button_text = add_to_cart_button.text
    print(f"✅ Кнопка найдена! Текст на кнопке: '{button_text}'")
    
    # Проверяем, что текст соответствует ожидаемому для разных языков
    # (этот тест будет проваливаться для не-английских языков,
    # что нам и нужно для сбора сообщений)
    expected_text = "Add to cart"
    assert button_text == expected_text, (
        f"\n❌ Неожиданный текст на кнопке!\n"
        f"   Ожидалось: '{expected_text}'\n"
        f"   Получено: '{button_text}'"
    )
    
    print("✅ Тест успешно пройден!")


def test_multiple_products_have_add_to_cart_buttons(browser):
    """
    Проверяем, что у всех товаров есть кнопки добавления в корзину
    """
    link = "https://www.saucedemo.com/inventory.html"
    browser.get(link)
    
    # Авторизация
    browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()
    
    # Ждем загрузки товаров
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item"))
    )
    
    # Находим все кнопки добавления в корзину
    add_to_cart_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn_inventory")
    
    # Проверяем, что кнопок столько же, сколько товаров
    inventory_items = browser.find_elements(By.CSS_SELECTOR, ".inventory_item")
    
    print(f"\n📊 Найдено товаров: {len(inventory_items)}")
    print(f"🔘 Найдено кнопок: {len(add_to_cart_buttons)}")
    
    assert len(add_to_cart_buttons) == len(inventory_items), (
        f"Количество кнопок ({len(add_to_cart_buttons)}) "
        f"не совпадает с количеством товаров ({len(inventory_items)})"
    )
    
    # Проверяем текст на каждой кнопке
    for i, button in enumerate(add_to_cart_buttons):
        button_text = button.text
        print(f"  Товар {i+1}: кнопка '{button_text}'")
        assert button.is_displayed(), f"Кнопка для товара {i+1} не отображается"
        assert button.is_enabled(), f"Кнопка для товара {i+1} неактивна"
    
    print("✅ Все товары имеют активные кнопки добавления в корзину")
