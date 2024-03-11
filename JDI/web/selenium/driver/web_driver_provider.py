from webdriver_manager.chrome import ChromeDriverManager
import sys

class WebDriverProvider:
    @staticmethod
    def get_chrome_driver_path():
        chrome = ChromeDriverManager().install()
        return chrome

