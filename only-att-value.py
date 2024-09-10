from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get('website')
driver.maximize_window()
def is_available(att,abd):
    try:
        driver.find_element(by=att,value=abd)
        return True
    except NoSuchElementException:
        return False
print(is_available(By.TAG_NAME,'a'))
print(is_available(By.XPATH,'option'))
print(is_available(By.TAG_NAME,'dev'))
