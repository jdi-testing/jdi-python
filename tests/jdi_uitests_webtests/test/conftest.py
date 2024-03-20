import logging

import pytest

from JDI.web.selenium.elements.composite.web_site import WebSite
from JDI.web.selenium.settings.web_settings import WebSettings
from tests.jdi_uitests_webtests.main.entities.user import User
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite

logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def site():
    WebSite.init(EpamJDISite)
    logger.info(f"Run Tests from '{__name__}' file, browser: {WebSettings.get_driver_factory().current_driver.name}")
    EpamJDISite.home_page.open()
    EpamJDISite.login_page.submit(User.default())

    yield

    try:
        WebSettings.quit_browser()
    except RuntimeError as e:
        logger.exception(e)
