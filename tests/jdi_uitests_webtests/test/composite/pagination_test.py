import pytest

from JDI.core.settings.jdi_settings import JDISettings
from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.test.init_tests import InitTests


def check_page_opened(verifier):
    Assert.assert_true(JDISettings.get_driver_factory().get_driver().current_url.endswith(verifier))


@pytest.mark.web
class PaginationTests(InitTests):
    pagination = EpamJDISite.simple_table_page.pagination

    def setUp(self):
        super(PaginationTests, self).setUp(self.id().split(".")[-1])
        Preconditions.SIMPLE_TABLE_PAGE.is_in_state()

    def test_next(self):
        self.pagination.first()
        self.pagination.next()
        check_page_opened("dates.html")

    def test_previous(self):
        self.pagination.last()
        self.pagination.previous()
        check_page_opened("table-pages.html")

    def test_first(self):
        self.pagination.first()
        check_page_opened("support.html")

    def test_last(self):
        self.pagination.last()
        check_page_opened("performance.html")
