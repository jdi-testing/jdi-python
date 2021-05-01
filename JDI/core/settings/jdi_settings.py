import logging
from pathlib import Path

logger = logging.Logger(__name__)


class PropertyPath:
    def __init__(self, filename="jdi.properties"):
        self._filename = Path(filename)

    def get_property_file(self):
        logger.info("Directory to search {dir_to_search}".format(dir_to_search=self._filename))
        if self._filename.exists():
            return self._filename
        else:
            raise FileNotFoundError("There is not property file with name '" + self._filename + "' in your project")


class JDISettings:

    JDI_SETTINGS_FILE_PATH = PropertyPath().get_property_file()

    __wait_element_sec = 20
    _driver_factory = None
    __logger = None
    _jdi_settings = dict()

    @staticmethod
    def get_driver_factory():
        return JDISettings._driver_factory

    @staticmethod
    def _read_jdi_settings():
        with open(JDISettings.JDI_SETTINGS_FILE_PATH) as f:
            JDISettings._jdi_settings = dict()
            for line in f.readlines():
                if not line.startswith("#"):
                    param = line.split("=")
                    JDISettings._jdi_settings[param[0]] = param[1].strip()

    @staticmethod
    def get_driver_path():
        return JDISettings.get_setting_by_name("drivers_folder")

    @staticmethod
    def get_setting_by_name(setting_name):
        if not JDISettings._jdi_settings:
            JDISettings._read_jdi_settings()
        return JDISettings._jdi_settings.get(setting_name, None)

    @staticmethod
    def get_current_timeout_sec():
        timeout_wait_element = JDISettings.get_setting_by_name("timeout_wait_element")
        return JDISettings.__wait_element_sec if timeout_wait_element is None else timeout_wait_element

    @staticmethod
    def get_domain():
        return JDISettings.get_setting_by_name("domain")
