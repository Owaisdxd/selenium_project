from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('')   # website  
def find_var(att,abd):
    if driver.find_element(by=att,value=abd) == 0:
        return False
    else:
        return True

print(find_var(By.TAG_NAME,'a'))
driver.quit()
