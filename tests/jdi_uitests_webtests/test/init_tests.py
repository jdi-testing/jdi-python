import logging
import unittest

from JDI.web.selenium.elements.composite.web_site import WebSite
from JDI.web.selenium.settings.web_settings import WebSettings
from tests.jdi_uitests_webtests.main.entities.user import User
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.page_objects.w3c_site.w3c_site import W3cSite

logger = logging.getLogger(__name__)


class InitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        WebSite.init(EpamJDISite)
        logger.info("Run Tests from '{}' file".format(cls.__name__))
        EpamJDISite.home_page.open()
        EpamJDISite.login_page.submit(User.default())

    @classmethod
    def setUp(cls, name=""):
        logger.info("Run Test '{}'".format(name))

    @classmethod
    def tearDownClass(cls):
        try:
            WebSettings.quit_browser()
        except RuntimeError as e:
            logging.exception(e)


class W3CInit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        WebSite.init(W3cSite)
        logger.info("Run Tests")
        W3cSite.frame_page.open()

    @classmethod
    def tearDownClass(cls):
        WebSettings.quit_browser()
