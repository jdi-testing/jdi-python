import pytest

from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.utils.common_action_data import CommonActionsData

MSG_TRUE = "Water: condition changed to true"
MSG_FALSE = "Water: condition changed to false"


@pytest.fixture
def checkbox_setup(site):
    Preconditions.METALS_AND_COLORS_PAGE.is_in_state()


@pytest.mark.web
class TestCheckBoxText:

    check_box = EpamJDISite.metals_colors_page.cb_water

    @staticmethod
    @pytest.mark.parametrize("input_value, expected", [("True", True), ("1", True), ("False", False), ("0", False)])
    def test_set_value(checkbox_setup, input_value, expected):
        if not expected:
            EpamJDISite.metals_colors_page.cb_water.click()
        EpamJDISite.metals_colors_page.cb_water.set_value(input_value)
        CommonActionsData.check_action("Water: condition changed to " + str(expected).lower())

    @pytest.mark.parametrize("input_value", ["true ", "1 ", " false", "0 ", " ", "123", " 1", " 0", "!@#$%^&*",
                                             "qwdewf", "1qwe", "1qwe", "true123", "123true", "false123", "123false",
                                             "o", "O", "tr ue", ])
    def test_set_value_nothing_changes(self, checkbox_setup, input_value):
        self.check_box.click()
        self.check_box.set_value(input_value)
        CommonActionsData.check_action(MSG_TRUE)
        self.check_box.click()
        self.check_box.set_value(input_value)
        CommonActionsData.check_action(MSG_FALSE)

    def test_check_single(self, checkbox_setup):
        self.check_box.check()
        CommonActionsData.check_action(MSG_TRUE)

    def test_uncheck_single(self, checkbox_setup):
        self.check_box.click()
        self.check_box.uncheck()
        CommonActionsData.check_action(MSG_FALSE)

    def test_is_check(self, checkbox_setup):
        Assert.assert_false(self.check_box.is_checked())
        self.check_box.click()
        Assert.assert_true(self.check_box.is_checked())

    def test_multi_uncheck(self, checkbox_setup):
        self.check_box.click()
        self.check_box.uncheck()
        self.check_box.uncheck()
        CommonActionsData.check_action(MSG_FALSE)

    def test_multi_check(self, checkbox_setup):
        self.check_box.check()
        self.check_box.check()
        CommonActionsData.check_action(MSG_TRUE)

    def test_click(self, checkbox_setup):
        self.check_box.click()
        CommonActionsData.check_action(MSG_TRUE)
        self.check_box.click()
        CommonActionsData.check_action(MSG_FALSE)