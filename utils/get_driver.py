from JDI.web.selenium.driver.selenium_driver_factory import SeleniumDriverFactory

if __name__ == "__main__":
    driver_factory = SeleniumDriverFactory()
    driver = driver_factory.get_driver()
    driver.quit()
