import pytest
import unittest
import logging
from JDI.web.selenium.settings.web_settings import WebSettings
from JDI.web.selenium.elements.composite.web_site import WebSite
from tests.jdi_uitests_webtests.main.entities.user import User
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.page_objects.w3c_site.w3c_site import W3cSite


@pytest.fixture(scope="class")
def site():
    WebSite.init(EpamJDISite)
    # TODO: Refactor logging here
    WebSettings.logger.info("\nRun Tests from '%s' file" % __name__)
    EpamJDISite.home_page.open()
    EpamJDISite.login_page.submit(User.default())

    yield

    try:
        WebSettings.quit_browser()
    except RuntimeError as e:
        logging.exception(e)