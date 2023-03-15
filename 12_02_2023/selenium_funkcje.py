from selenium import webdriver
import time
import datetime

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)