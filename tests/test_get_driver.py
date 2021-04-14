import os

import pytest

from utils import get_driver


@pytest.mark.unit
class TestChrome:
    def test_download_chromedriver(self):
        get_driver.download_driver("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip")
        assert os.path.exists("chromedriver_win32.zip") is True
        assert os.path.exists("chromedriver.exe") is True

    def test_get_last_release(self):
        assert get_driver.get_last_release() == "89.0.4389.23"

    def test_get_last_release_for_build(self):
        assert get_driver.get_last_release(build="87") == "87.0.4280.88"

    def test_compose_driver_download_link(self):
        assert (
            get_driver.compose_download_link("89.0.4389.23")
            == "https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip"
        )
