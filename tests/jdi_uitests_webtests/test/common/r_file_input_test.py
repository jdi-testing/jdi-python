import sys

import pytest

from JDI.jdi_assert.testing.assertion import Assert
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.epam_jdi_site import \
    EpamJDISite
from tests.jdi_uitests_webtests.main.utils.common_action_data import \
    CommonActionsData
from tests.jdi_uitests_webtests.test.init_tests import InitTests


# Probably it's possible to use JS for drag'n'drop
@pytest.mark.skipif(sys.platform != "win32", reason="works on Windows only")
@pytest.mark.web
class RFileInputTests(InitTests):
    text_file = EpamJDISite.dates_page.r_image_input
    uploaded_file_name = EpamJDISite.dates_page.uploaded_file_name

    def setUp(self):
        super(RFileInputTests, self).setUp(self.id().split(".")[-1])
        Preconditions.DATES_PAGE.is_in_state()

    def test_input(self):
        self.text_file.input(CommonActionsData.get_file_path())
        self.check_file_loaded(CommonActionsData.get_file_name())

    def test_send_keys(self):
        self.text_file.send_keys(CommonActionsData.get_file_path())
        self.check_file_loaded(CommonActionsData.get_file_name())

    def test_new_input_test(self):
        self.text_file.new_input(CommonActionsData.get_file_path())
        self.check_file_loaded(CommonActionsData.get_file_name())

    def check_file_loaded(self, file_name):
        CommonActionsData.check_action('FileUpload: file "{0}" has been uploaded'.format(file_name))
        Assert.assert_contains(self.uploaded_file_name.get_text(), file_name)
