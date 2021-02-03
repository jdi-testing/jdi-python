from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.entities import Odds
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.utils.common_action_data import CommonActionsData
from tests.jdi_uitests_webtests.test.init_tests import InitTests
from tests.jdi_uitests_webtests.main.page_objects.sections.summary import SelectorSummary


MSG = "Summary (Odd): value changed to 7"

import pytest


@pytest.fixture
def selector_site(site):
    Preconditions.METALS_AND_COLORS_PAGE.is_in_state()


@pytest.mark.web
@pytest.mark.parametrize(
    "radio_buttons",
    [
        EpamJDISite.metals_colors_page.summary.odds_selector,
        EpamJDISite.metals_colors_page.summary.odds_radio_buttons,
    ],
    ids=["Selectors", "Radio Buttons"],
)
class TestSelector:
    odd_options = ["1", "3", "5", "7"]

    def test_select_string(self, selector_site, radio_buttons):
        radio_buttons.select("7")
        CommonActionsData.check_action(MSG)

    def test_select_index(self, selector_site, radio_buttons):
        radio_buttons.select(4)
        CommonActionsData.check_action(MSG)

    def test_select_enum(self, selector_site, radio_buttons):
        radio_buttons.select(Odds.SEVEN)
        CommonActionsData.check_action(MSG)

    def test_get_options(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.get_options(), self.odd_options)

    def test_get_names(self, radio_buttons):
        Assert.assert_equal(radio_buttons.get_names(), self.odd_options)

    def test_get_values(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.get_values(), self.odd_options)

    def test_get_options_as_text(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.get_options_as_text(), ", ".join(self.odd_options))

    def test_set_value_text(self, selector_site, radio_buttons):
        radio_buttons.set_value("7")
        CommonActionsData.check_action(MSG)

    def test_get_name(self, selector_site, radio_buttons):
        Assert.assert_equal(
            radio_buttons.get_name(),
            "odds_selector" if isinstance(radio_buttons, SelectorSummary) else "odds_radio_buttons",
        )

    def test_get_selected(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.get_selected(), "1")

    def test_get_selected_index(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.get_selected_index(), 0)

    def test_is_selected(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.is_selected("7"), False)
        Assert.assert_equal(radio_buttons.is_selected("1"), True)

    def test_is_selected_enum(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.is_selected(Odds.SEVEN), False)
        Assert.assert_equal(radio_buttons.is_selected(Odds.ONE), True)

    def test_get_value(self, selector_site, radio_buttons):
        Assert.assert_equal(radio_buttons.get_value(), "1")
