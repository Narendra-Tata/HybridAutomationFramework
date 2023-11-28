'''
Created on 2023-Nov-5
@author: Narendra Tata
'''
import pytest
from selenium import webdriver
driver = None
import time
import settings
from AUT.ATGFR8.actions import *
from selenium_framework.utils import *


def BasicTest():
    url = get_url()
    browser_name = get_browser()
    global driver

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
    elif browser_name == "IE":
        driver = webdriver.Firefox(executable_path="./drivers/msedgedriver")

    driver.get(url)
    driver.maximize_window()
    username_input = driver.find_element_by_name('Email')
    username_input.send_keys('parvesh.kumar@aithinkers.com')
    password_input = driver.find_element_by_name('Password')
    password_input.send_keys('Heer@11july')
    login_button = driver.find_element_by_class('btn btn-primary')
    login_button.click()
    driver.quit()


def test1():
    print("Test 1")
    return 'pass'


def test2():
    print("Test 2")
    return 'fail'


