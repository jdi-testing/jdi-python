from enum import Enum

from selenium.webdriver.chrome.webdriver import WebDriver

from JDI.core.settings.jdi_settings import JDISettings
from JDI.web.selenium.preconditions.web_preconditions import WebPreconditions


class Preconditions(str, Enum):
    HOME_PAGE = ("/index.html",)
    CONTACT_PAGE = ("/contacts.html",)
    METALS_AND_COLORS_PAGE = ("/metals-colors.html",)
    SUPPORT_PAGE = ("/support.html",)
    DATES_PAGE = "/dates.html"
    SIMPLE_TABLE_PAGE = "/simple-table.html"

    def is_in_state(self):
        str_value = self.value[0] if isinstance(self.value, tuple) else self.value
        if not WebPreconditions.check_url(str_value):
            WebPreconditions.open_uri(JDISettings.get_domain() + str_value)
