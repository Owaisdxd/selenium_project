import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    """
    This script initializes a headless Chrome browser using Selenium WebDriver,
    navigates to the Selenium website, prints the title of the page, and then
    closes the browser after a short delay.

    Steps performed:
    1. Configure ChromeOptions to run in headless mode.
    2. Initialize the Chrome WebDriver with the specified options.
    3. Open the Selenium website.
    4. Maximize the browser window.
    5. Set an implicit wait of 10 seconds.
    6. Print the title of the page.
    7. Wait for 5 seconds to observe the result.
    8. Close the browser.

    Exceptions:
    If any exceptions occur during the execution, an error message is printed.
    """

    try:
        # Configure ChromeOptions to run in headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        
        # Initialize the Chrome WebDriver with the specified options
        driver = webdriver.Chrome(options=chrome_options)
        
        # Navigate to the Selenium website
        driver.get('https://www.selenium.dev/')
        
        # Maximize the browser window
        driver.maximize_window()
        
        # Set an implicit wait time of 10 seconds
        driver.implicitly_wait(10)
        
        # Print the title of the current page
        print(driver.title)
        
        # Wait for 5 seconds to observe the result
        time.sleep(5)
        
        # Close the browser
        driver.quit()

    except Exception as e:
        # Print the exception message if an error occurs
        print("Please refer to the issue:", e)

# Execute the main function
if __name__ == "__main__":
    main()
