from selenium import webdriver
import time
import datetime

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)

    driver = webdriver.Chrome()
    driver.get('http://www.saucedemo.com/')
    print('Nazwa strony ',driver.title)
    try:
        pole_user = driver.find_element('id','user-name')
        pole_user.clear()
        pole_user.send_keys('standard_user')
    except:
        make_screenshot(driver)
        pole_haslo = driver.find_element('xpath','//*[@id="password"]')
        pole_haslo.clear()
        pole_haslo.send_keys('secret_sauce')
        przycisk_login = driver.find_element('id','login-button')# print(przycisk_login.get_attribute('enabled'))# if przycisk_login.get_attribute('disabled'):przycisk_login.click()time.sleep(2)make_screenshot(driver)driver.quit()Selenium2 Pythonfrom selenium import webdriverimport timeimport datetimedef make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)
driver = webdriver.Chrome()
driver.get('http://www.saucedemo.com/')
print('Nazwa strony ',driver.title)
try:
    pole_user = driver.find_element('id','user-name')
    pole_user.clear()
    pole_user.send_keys('standard_user')
except:
    make_screenshot(driver)
pole_haslo = driver.find_element('xpath','//*[@id="password"]')
pole_haslo.clear()
pole_haslo.send_keys('secret_sauce')
przycisk_login = driver.find_element('id','login-button')
# print(przycisk_login.get_attribute('enabled'))# if przycisk_login.get_attribute('disabled'):przycisk_login.click()
time.sleep(2)
make_screenshot(driver)
driver.quit()