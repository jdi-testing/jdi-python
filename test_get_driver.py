import unittest
import get_driver
import os


class ChromeTest(unittest.TestCase):
    def test_download_chromedriver(self):
        get_driver.download_driver(
            "https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_win32.zip"
        )
        self.assertTrue(os.path.exists("chromedriver_win32.zip"))
        self.assertTrue(os.path.exists("chromedriver.exe"))

    def test_get_last_release(self):
        self.assertEqual(get_driver.get_last_release(), "88.0.4324.96")

    def test_get_last_release_for_build(self):
        self.assertEqual(get_driver.get_last_release(build="87"), "87.0.4280.88")

    def test_compose_driver_download_link(self):
        self.assertEqual(
            get_driver.compose_download_link("88.0.4324.96"),
            "https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_win32.zip",
        )


if __name__ == "__main__":
    unittest.main()
