import pickle
import unittest

import pytest

from JDI.core.settings.jdi_settings import JDISettings
from JDI.jdi_assert.testing.assertion import Assert
from JDI.web.selenium.elements.composite.web_site import WebSite
from JDI.web.selenium.settings.web_settings import WebSettings
from tests.jdi_uitests_webtests.main.entities.user import User
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite

import logging

logger = logging.getLogger(__name__)

@pytest.mark.web
class PageTests(unittest.TestCase):
    def setUp(self):
        logger.info("Run Test %s" % self.id().split(".")[-1])
        WebSite.init(EpamJDISite)
        logger.info("Run Tests")
        EpamJDISite.home_page.open()
        EpamJDISite.login_page.submit(User.default())
        Preconditions.CONTACT_PAGE.is_in_state()

    def test_refresh(self):
        EpamJDISite.contact_form_page.contact_form.submit.click()
        Assert.assert_equal(EpamJDISite.contact_form_page.result.get_text(), "Summary: 3")
        EpamJDISite.contact_form_page.refresh()
        Assert.assert_equal(EpamJDISite.contact_form_page.result.get_text(), "")
        EpamJDISite.contact_form_page.check_opened()

    def test_back(self):
        EpamJDISite.home_page.open()
        EpamJDISite.home_page.check_opened()
        EpamJDISite.home_page.back()
        EpamJDISite.contact_form_page.check_opened()

    def test_forward(self):
        EpamJDISite.home_page.open()
        EpamJDISite.home_page.back()
        EpamJDISite.contact_form_page.check_opened()
        EpamJDISite.contact_form_page.forward()
        EpamJDISite.home_page.check_opened()

    def test_add_cookie(self):
        cookie = {"name": "key", "value": "value"}
        self.get_driver().delete_all_cookies()
        Assert.assert_true(not len(self.get_driver().get_cookies()))
        EpamJDISite.contact_form_page.add_cookie(cookie)
        Assert.assert_equal(self.get_driver().get_cookie(cookie["name"])["value"], cookie["value"])

    def test_clear_cache(self):
        cookie = {"name": "key", "value": "value"}
        EpamJDISite.contact_form_page.add_cookie(cookie)
        Assert.assert_false(not len(self.get_driver().get_cookies()))
        EpamJDISite.contact_form_page.clear_cache()
        Assert.assert_true(not len(self.get_driver().get_cookies()))

    def tearDown(self):
        WebSettings.quit_browser()

    def get_driver(self):
        return JDISettings.get_driver_factory().get_driver()
