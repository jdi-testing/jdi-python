from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.entities.contact import Contact
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import EpamJDISite
from tests.jdi_uitests_webtests.test.init_tests import InitTests
import pytest


@pytest.mark.web
class FormTwoButtonsTests(InitTests):
    form = EpamJDISite.contact_form_page.contact_form_two_buttons
    contact = Contact("Ivan", "Ivanov", "Smart Man")

    def setUp(self):
        super(FormTwoButtonsTests, self).setUp(self.id().split(".")[-1])
        Preconditions.CONTACT_PAGE.is_in_state()

    def test_submit_spec_button_string(self):
        self.form.submit_form(self.contact, "calculate")
        Assert.wait_assert_equal(lambda: EpamJDISite.contact_form_page.result.get_text(), str(self.contact))
