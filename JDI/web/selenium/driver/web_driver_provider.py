import os
import sys

from JDI.core.settings.jdi_settings import JDISettings


class WebDriverProvider:
    @staticmethod
    def get_chrome_driver_path():
        chrome = ".\chromedriver.exe" if sys.platform.startswith("win") else "chromedriver"
        return os.path.join(JDISettings.get_driver_path(), chrome)
