import pytest

from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite


@pytest.mark.web
class TestButton:

    button = EpamJDISite.metals_colors_page.calculate_button

    def test_click(self, epam_site):
        Preconditions.METALS_AND_COLORS_PAGE.is_in_state()
        self.button.click()
        Assert.assert_element_test(self.button, "CALCULATE")
