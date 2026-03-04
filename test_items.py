@"
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_basket_button_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(2)
    
    button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket'))
    )
    assert button.is_displayed(), 'Button not found!'
    assert button.is_enabled(), 'Button is disabled!'
    
    print(f'\nButton text: {button.text}')
"@ | Out-File -FilePath test_items.py -Encoding UTF8
