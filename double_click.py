import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()  #selecting the browser
driver.get('https:yourwebsite')

driver.maximize_window()
driver.implicitly_wait(20)    #it will wait for the site to responde if it did not in responde in 20 sec it will move on this will be applied in the whole code
action=ActionChains(driver)  
myvar= driver.find_element(By.XPATH,'Xpath')
time.sleep(5)
action.double_click(myvar).perform()
time.sleep(5)                          #double click example


driver.quit()



