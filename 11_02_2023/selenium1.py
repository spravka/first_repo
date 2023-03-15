from selenium import webdriver
import time
import datetime

teraz = datetime.datetime.now()
screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'

driver = webdriver.Chrome()
driver.get('https://saucedemo.com')
print('Nazwa strony ',driver.title)
print(screenshot)
pole_user = driver.find_element('id', 'user-name')
pole_user.clear()
pole_user.send_keys('standard_user')

pole_haslo = driver.find_element('id', 'password')
pole_user.clear()
pole_haslo.send_keys('secret_sauce')

przycisk_login = driver.find_element('id', 'login-button')
przycisk_login.click()

time.sleep(2)
driver.get_screenshot_as_file('screenshot.png')
driver.quit()

# button1_accept = driver.find_element('id', 'L2AGLb')
# button1_accept.click()
# # print(button1_accept)
# pole_szukaj = driver.find_element('name', 'q')
# pole_szukaj.send_keys('eesti vabariik')
# przycisk_szukaj = driver.find_element('name', 'btnK')
# przycisk_szukaj.submit()
# time.sleep(60)
# driver.quit()