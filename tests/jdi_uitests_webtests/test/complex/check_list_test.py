import pytest

from selenium.webdriver.common.by import By

from JDI.core.settings.jdi_settings import JDISettings
from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.entities import Nature
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.main.utils.common_action_data import CommonActionsData

FIRE_MSG = "Fire: condition changed to true"
WATER_MSG = "Water: condition changed to true"


@pytest.fixture
def check_list_setup(site):
    Preconditions.METALS_AND_COLORS_PAGE.is_in_state()


@pytest.mark.web
class TestCheckList:
    nature_options = ["Water", "Earth", "Wind", "Fire"]
    all_values = "Water, Earth, Wind, Fire"

    check_list = EpamJDISite.metals_colors_page.nature_check_list

    @pytest.mark.parametrize("value", ("Fire", 4, Nature.FIRE))
    def test_select(self, check_list_setup, value):
        self.check_list.select(value)
        CommonActionsData.check_action(FIRE_MSG)

    def test_select_2_string(self, check_list_setup):
        self.check_list.select("Water", "Fire")
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action(WATER_MSG, line_number=1)

    def test_select_2_index(self, check_list_setup):
        self.check_list.select(1, 4)
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action(WATER_MSG, line_number=1)

    def test_select_2_enum(self, check_list_setup):
        self.check_list.select(Nature.WATER, Nature.FIRE)
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action(WATER_MSG, line_number=1)

    @pytest.mark.parametrize("value", ("Fire", 4, Nature.FIRE))
    def test_check(self, check_list_setup, value):
        self.check_list.check(value)
        CommonActionsData.check_action(FIRE_MSG)

    def test_check_2_string(self, check_list_setup):
        self.check_list.check("Water", "Fire")
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action(WATER_MSG, line_number=1)

    def test_check_2_index(self, check_list_setup):
        self.check_list.check(1, 4)
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action(WATER_MSG, line_number=1)

    def test_check_2_enum(self, check_list_setup):
        self.check_list.check(Nature.WATER, Nature.FIRE)
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action(WATER_MSG, line_number=1)

    def test_select_all(self, check_list_setup):
        self.check_list.select_all()
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action("Wind: condition changed to true", line_number=1)
        CommonActionsData.check_action("Earth: condition changed to true", line_number=2)
        CommonActionsData.check_action(WATER_MSG, line_number=3)
        self.check_all_checked()

    def test_check_all(self, check_list_setup):
        self.check_list.check_all()
        CommonActionsData.check_action(FIRE_MSG, line_number=0)
        CommonActionsData.check_action("Wind: condition changed to true", line_number=1)
        CommonActionsData.check_action("Earth: condition changed to true", line_number=2)
        CommonActionsData.check_action(WATER_MSG, line_number=3)
        self.check_all_checked()

    def test_clear_all(self, check_list_setup):
        self.check_list.check_all()
        self.check_all_checked()
        self.check_list.clear()
        self.check_all_unchecked()

    def test_uncheck_all(self, check_list_setup):
        self.check_list.check_all()
        self.check_all_checked()
        self.check_list.uncheck_all()
        self.check_all_unchecked()

    def test_get_options(self, check_list_setup):
        Assert.assert_equal(self.check_list.get_options(), self.nature_options)

    def test_get_names(self, check_list_setup):
        Assert.assert_equal(self.check_list.get_names(), self.nature_options)

    def test_get_values(self, check_list_setup):
        Assert.assert_equal(self.check_list.get_values(), self.nature_options)

    def test_get_options_as_text(self, check_list_setup):
        Assert.assert_equal(self.check_list.get_options_as_text(), self.all_values)

    def test_set_value(self, check_list_setup):
        self.check_list.set_value("Fire")
        CommonActionsData.check_action(FIRE_MSG)

    def test_get_name(self, check_list_setup):
        Assert.assert_equal(self.check_list.get_name(), "nature_check_list")

    def test_are_selected(self, check_list_setup):
        Assert.assert_equal(self.check_list.are_selected(), [])

    def test_are_deselected(self, check_list_setup):
        Assert.assert_equal(self.check_list.are_deselected(), self.nature_options)

    def test_get_value(self, check_list_setup):
        Assert.assert_equal(self.check_list.get_value(), None)

    def check_all_checked(self):
        driver = JDISettings.get_driver_factory().get_driver()
        els = driver.find_elements(By.CSS_SELECTOR, value="#elements-checklist input")
        for el in els:
            Assert.assert_true(el.get_attribute("checked") == "true")

    def check_all_unchecked(self):
        driver = JDISettings.get_driver_factory().get_driver()
        els = driver.find_elements(By.CSS_SELECTOR, value="#elements-checklist input")
        for el in els:
            Assert.assert_true(el.get_attribute("checked") in ["false", None])
