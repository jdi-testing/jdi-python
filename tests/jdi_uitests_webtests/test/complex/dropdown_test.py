import pytest

from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.entities import Colors
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.utils.common_action_data import CommonActionsData

MSG = "Colors: value changed to Blue"


@pytest.fixture(params=[True, False], ids=["Dropdown", "Dropdown expanded"])
def dropdown_setup(request, epam_site):
    dropdown = EpamJDISite.metals_colors_page.color_dropdown
    Preconditions.METALS_AND_COLORS_PAGE.is_in_state()
    if request.param:
        dropdown.expand()

    yield dropdown


@pytest.mark.web
class TestDropdown:

    odd_options = ["Colors", "Red", "Green", "Blue", "Yellow"]

    def test_select_string(self, dropdown_setup):
        dropdown_setup.select("Blue")
        CommonActionsData.check_action(MSG)

    def test_select_index(self, dropdown_setup):
        dropdown_setup.select(4)
        CommonActionsData.check_action(MSG)

    def test_select_enum(self, dropdown_setup):
        dropdown_setup.select(Colors.BLUE)
        CommonActionsData.check_action(MSG)

    def test_get_options(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.get_options(), self.odd_options)

    def test_get_names(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.get_names(), self.odd_options)

    def test_get_values(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.get_values(), self.odd_options)

    def test_get_options_as_text(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.get_options_as_text(), "Colors, Red, Green, Blue, Yellow")

    def test_set_value(self, dropdown_setup):
        dropdown_setup.set_value("Blue")
        CommonActionsData.check_action(MSG)

    def test_get_name(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.get_name(), "color_dropdown")

    def test_get_selected(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.get_selected(), "Colors")

    def test_get_selected_index(self, dropdown_setup):
        CommonActionsData.check_action_throw_error(
            lambda: dropdown_setup.get_selected_index(), CommonActionsData.no_elements_message()
        )

    def test_is_selected(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.is_selected("Colors"), True)

    def test_is_selected_enum(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.is_selected(Colors.COLORS), True)

    def test_get_value(self, dropdown_setup):
        Assert.assert_equal(dropdown_setup.get_value(), "Colors")
