import pytest

from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.test.init_tests import InitTests


@pytest.mark.web
class SearchTests(InitTests):
    def setUp(self):
        super(SearchTests, self).setUp(self.id().split(".")[-1])
        Preconditions.HOME_PAGE.is_in_state()

    def test_fill(self):
        EpamJDISite.header.search_section.find("something")
        EpamJDISite.search_page.check_opened()
