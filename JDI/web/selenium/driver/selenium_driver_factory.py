import os

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver

from JDI.core.settings.jdi_settings import JDISettings
from JDI.web.selenium.driver.driver_types import DriverTypes
from JDI.web.selenium.driver.web_driver_provider import WebDriverProvider


class SeleniumDriverFactory:

    def __init__(self):
        self.options = None
        self.current_driver = None
        self.browser_size = None
        self.drivers_path = JDISettings.get_driver_path()
        self.capabilities = {}

    def register_driver(self, driver_name, options, capabilities, executor):
        driver_name = driver_name.lower()
        self.set_driver_options_and_capabilities(driver_name, options, capabilities, executor)
        if executor is not None:
            self.current_driver = self.register_remote_driver(executor)
        else:
            if driver_name == DriverTypes.chrome.name:
                self.current_driver = self.register_chrome_driver()
            if driver_name == DriverTypes.firefox.name:
                self.current_driver = self.register_firefox_driver()
        return driver_name

    def set_driver_options_and_capabilities(self, driver_name, options, capabilities, executor):
        if driver_name == DriverTypes.chrome.name:
            self.options = ChromeOptions()
            # TODO: move hardcoded arguments to params
            self.options.add_argument("start-maximized")
            self.options.add_argument("disable-gpu")
            self.add_options(options) if options else True
            if not capabilities and executor is not None:
                self.capabilities = DesiredCapabilities.CHROME
        if driver_name == DriverTypes.firefox.name:
            self.options = FirefoxOptions()
            self.add_options(options) if options else True
            if not capabilities and executor is not None:
                self.capabilities = DesiredCapabilities.FIREFOX
        if capabilities:
            self.capabilities = capabilities

    def add_options(self, options):
        for arg in options:
            self.options.add_argument(arg)

    def register_chrome_driver(self):
        chrome_driver = WebDriverProvider.get_chrome_driver_path()
        os.environ["webdriver.chrome.driver"] = chrome_driver
        return self.__web_driver_settings(ChromeDriver(executable_path=chrome_driver,
                                                       options=self.options,
                                                       desired_capabilities=self.capabilities))

    def register_firefox_driver(self):
        raise NotImplementedError

    def register_remote_driver(self, executor):
        chrome_driver = WebDriverProvider.get_chrome_driver_path()
        os.environ["webdriver.chrome.driver"] = chrome_driver
        driver = self.__web_driver_settings(RemoteDriver(command_executor=executor,
                                                         options=self.options,
                                                         desired_capabilities=self.capabilities,
                                                         keep_alive=True))
        return driver

    def __web_driver_settings(self, driver):
        if self.browser_size is None:
            driver.maximize_window()
        else:
            driver.set_window_size(self.browser_size)
        driver.implicitly_wait(JDISettings.get_current_timeout_sec())
        return driver

    def get_driver(self, options=None, capabilities=None, executor=None):
        if self.current_driver is not None:
            return self.current_driver
        else:
            self.register_driver(driver_name=DriverTypes.chrome.name,
                                 options=options,
                                 capabilities=capabilities,
                                 executor=executor)
            return self.current_driver
