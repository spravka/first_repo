from selenium import webdriver
from selenium_funkcje import make_screenshot
from selenium4 import LoginPage
import time

import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]
@pytest.mark.parametrize('user, password, url', test_data)
def test_login_page(user, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(user)
    page.enter_password(password)
    page.click_login_button()
    time.sleep(1)
    try:
        assert driver.current_url == url, make_screenshot(driver)
    finally:
        driver.quit()