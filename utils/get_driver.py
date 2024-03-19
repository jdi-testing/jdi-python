from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def setup_chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

if __name__ == "__main__":
    driver = setup_chrome_driver()
    driver.quit()
