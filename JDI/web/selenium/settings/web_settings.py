from JDI.core.settings.jdi_settings import JDISettings
from JDI.web.selenium.driver.selenium_driver_factory import SeleniumDriverFactory
from JDI.core.logger.jdi_logger import JDILogger
from selenium.webdriver.remote.command import Command


class WebSettings(JDISettings):

    logger = JDILogger()
    domain = JDISettings.get_domain()

    @staticmethod
    def get_driver_factory():
        return JDISettings.get_driver_factory()

    @staticmethod
    def set_driver_factory(driver_factory):
        JDISettings._driver_factory = driver_factory

    @staticmethod
    def use_driver(options=None, capabilities=None, executor=None):
        driver_name = JDISettings.get_setting_by_name("driver")
        JDISettings._driver_factory = SeleniumDriverFactory()
        WebSettings.set_driver_factory(JDISettings._driver_factory)
        return JDISettings._driver_factory.register_driver(driver_name, options, capabilities, executor)

    @staticmethod
    def quit_browser():
        driver = WebSettings.get_driver_factory().get_driver()
        driver.quit()
        try:
            driver.execute(Command.CLOSE)
        except Exception:
            pass

    @staticmethod
    def get_driver():
        return WebSettings.get_driver_factory().get_driver()
