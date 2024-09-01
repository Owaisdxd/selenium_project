import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/v1/index.html')
driver.maximize_window()
web_name = driver.title
print("Website name is ",web_name)


time.sleep(5)
#Enter the username(value)
myusername = driver.find_element(By.ID,"user-name")
myusername.send_keys("standard_user")


time.sleep(5)
#Enter the password (value)
passwd = driver.find_element(By.ID,"password")
passwd.send_keys("secret_sauce")

time.sleep(5)
#click the button for login
mylogin = driver.find_element(By.ID,"login-button")
mylogin.click()

time.sleep(5)
#click the bar
click_side = driver.find_element(By.XPATH,'//*[@id="menu_button_container"]/div/div[3]/div/button')
click_side.click()


time.sleep(5)
#log out from the website
log_out = driver.find_element(By.ID,"logout_sidebar_link")
log_out.click()
time.sleep(5)

#close the window
driver.quit()
