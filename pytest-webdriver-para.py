import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_function(): #Establishing the connection and starting the testing
    global driver
    driver= webdriver.Chrome()
    driver.get('website')  # I have selected a website which requires username and password
    driver.maximize_window()

def teardown_function(): #Quiting the pytest testing with selenium
    global driver
    time.sleep(10)
    driver.quit()

def cred():# I have stored the multiple username and password (parameters)
    cred = [
        ('username1@email.com','passone'),
        ('username2@email.com','passtwo'),
        ('username3@email.com','passthree')
    ]
    return cred
@pytest.mark.parametrize('username,password',cred())
def test_return(username,password):
    global driver
    time.sleep(1)
    driver.find_element(By.NAME,'email').send_keys(username)
    time.sleep(2)
    driver.find_element(By.NAME,'password').send_keys(password)
    time.sleep(2)
