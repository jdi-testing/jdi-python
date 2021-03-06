import unittest
import logging
from JDI.web.selenium.settings.web_settings import WebSettings
from JDI.web.selenium.elements.composite.web_site import WebSite
from tests.jdi_uitests_webtests.main.entities.user import User
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.page_objects.w3c_site.w3c_site import W3cSite


class InitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        WebSite.init(EpamJDISite)
        WebSettings.logger.info("\nRun Tests from '%s' file" % cls.__name__)
        EpamJDISite.home_page.open()
        EpamJDISite.login_page.submit(User.default())

    @classmethod
    def setUp(cls, name=""):
        WebSettings.logger.info("\nRun Test '%s'" % name)

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
        WebSettings.logger.info("Run Tests")
        W3cSite.frame_page.open()

    @classmethod
    def tearDownClass(cls):
        WebSettings.quit_browser()