import logging
import unittest

import pytest

from JDI.web.selenium.elements.composite.web_site import WebSite
from JDI.web.selenium.settings.web_settings import WebSettings
from tests.jdi_uitests_webtests.main.entities.user import User
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.page_objects.w3c_site.w3c_site import W3cSite


logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def site():
    WebSite.init(EpamJDISite)
    logger.info("Run Tests from '{}' file".format(__name__))
    EpamJDISite.home_page.open()
    EpamJDISite.login_page.submit(User.default())

    yield

    try:
        WebSettings.quit_browser()
    except RuntimeError as e:
        logger.exception(e)
