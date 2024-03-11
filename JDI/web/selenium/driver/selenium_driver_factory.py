from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver

from JDI.core.settings.jdi_settings import JDISettings
from JDI.web.selenium.driver.driver_types import DriverTypes


class SeleniumDriverFactory:

    def __init__(self):
        self.options = None
        self.current_driver = None
        self.browser_size = None
        self.capabilities = {}

    def register_driver(self, driver_name, options, capabilities, executor):
        driver_name = driver_name.lower()
        self.set_driver_options_and_capabilities(driver_name, options, capabilities, executor)
        if executor is not None:
            self.current_driver = self.register_remote_driver(executor)
        else:
            if driver_name == DriverTypes.chrome.name:
                self.current_driver = self.register_chrome_driver()
        return driver_name

    def set_driver_options_and_capabilities(self, driver_name, options, capabilities, executor):
        if driver_name == DriverTypes.chrome.name:
            self.options = ChromeOptions()
            self.options.add_argument("start-maximized")
            self.options.add_argument("disable-gpu")
            if options:
                self.add_options(options)
            if not capabilities and executor is None:
                self.capabilities = DesiredCapabilities.CHROME
        if capabilities:
            self.capabilities = capabilities

    def add_options(self, options):
        for arg in options:
            self.options.add_argument(arg)

    def register_chrome_driver(self):
        service = Service(ChromeDriverManager().install())
        return self.__web_driver_settings(ChromeDriver(service=service,
                                                       options=self.options))

    def register_remote_driver(self, executor):
        driver = self.__web_driver_settings(RemoteDriver(command_executor=executor,
                                                         options=self.options,
                                                         keep_alive=True))
        return driver

    def __web_driver_settings(self, driver):
        if self.browser_size:
            driver.set_window_size(*self.browser_size)
        else:
            driver.maximize_window()
        driver.implicitly_wait(JDISettings.get_current_timeout_sec())
        return driver

    def get_driver(self, options=None, capabilities=None, executor=None):
        if not self.current_driver:
            self.register_driver(driver_name=DriverTypes.chrome.name,
                                 options=options,
                                 capabilities=capabilities,
                                 executor=executor)
        return self.current_driver
