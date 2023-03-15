from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from selenium_funkcje import make_screenshot
from selenium.common.exceptions import TimeoutException

def czekaj_na_id(element_id):
    timeout = 10
    timeout_message = f'Element o id {element_id} nie pojawil sie w czasie {timeout} s.'
    lokalizator = ('id', element_id) #szukanie po id konkretnej wartosci
    znaleziono = excon.visibility_of_element_located(lokalizator) #patyk do dźgania strony
    #obiekt bedzie pytany, czy jest ok, a odpowiedz bedzie zalezec od tego, czy element jest widoczny
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)

opcje = webdriver.ChromeOptions()
opcje.add_argument('headless')
driver = webdriver.Chrome(options=opcje)
driver.get('http://www.saucedemo.com/')
try:
    login_button = czekaj_na_id('login-button')
except TimeoutException:
    print('Nie znaleziono') #napisz cos
    raise #i tak zglos blad
else:
    print('Znaleziono')
finally: #pomimo bledu, wykonaj kolejne kroki
    make_screenshot(driver)
    time.sleep(2)
    driver.quit()
