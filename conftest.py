import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Добавляем параметр командной строки --language"""
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: ru, en, es, fr, etc.'
    )

@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для запуска браузера с указанным языком"""
    # Получаем параметр language из командной строки
    user_language = request.config.getoption("language")
    
    # Настраиваем опции Chrome для указанного языка
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    
    # Создаем браузер с указанными опциями
    print(f"\n🚀 Запуск браузера с языком: {user_language}")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    
    # Возвращаем браузер для использования в тестах
    yield browser
    
    # Закрываем браузер после теста
    print("\n🛑 Закрытие браузера")
    browser.quit()
