import pytest

from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.test.init_tests import InitTests


@pytest.mark.web
class ButtonTests(InitTests):

    button = EpamJDISite.metals_colors_page.calculate_button

    def setUp(self):
        super(ButtonTests, self).setUp(self.id().split(".")[-1])
        Preconditions.METALS_AND_COLORS_PAGE.is_in_state()

    def test_click(self):
        self.button.click()
        Assert.assert_element_test(self.button, "CALCULATE")
