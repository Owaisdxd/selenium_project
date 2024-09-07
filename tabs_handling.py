from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#how we can handle tabs
try:
    driver = webdriver.Chrome() #selecting the chrome
    driver.implicitly_wait(20)

    driver.get('Website') #select the website

    driver.maximize_window()

    driver.find_element(By.XPATH,'XPATH').click()  #path to the link inside the website

    winds = driver.window_handles

    print("Main Site",winds[0])
    print("Site inside the site",winds[1])
  
    time.sleep(5)

    driver.quit()
except Exception as e:
    print("Please refer to the issue",e)
