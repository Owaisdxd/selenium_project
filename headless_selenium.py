import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
try:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.selenium.dev/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    print(driver.title)
    time.sleep(5)
    driver.quit()
except Exception as e:
    print("Please refer to the issue",e)
