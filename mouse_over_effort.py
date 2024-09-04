import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver= webdriver.Edge()  #iam using edge you can use other as well

driver.get('')  #website that has the mouse over effect
driver.maximize_window()

menu_bar=driver.find_element(By.XPATH,'XPATH')
time.sleep(5)
action=ActionChains(driver)         #import ActionChains for mouse over effect will not work
action.move_to_element(menu_bar).perform()
driver.find_element(By.XPATH,'XPATH').click()
time.sleep(5)
time.sleep(20)
driver.quit()
