from __future__ import print_function

from JDI.jdi_assert.base.base_matcher import BaseMatcher
import os

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class PropertyPath:
    def get_property_file(self, file_name_init="jdi.properties"):
        file_name = file_name_init
        i = 0
        dir_to_search = os.getcwd()
        print(dir_to_search)
        while True and i < 100:
            try:
                open(file_name)
                return file_name
            except FileNotFoundError:
                dir_to_search = os.path.dirname(dir_to_search)
                file_name = os.path.join(dir_to_search, file_name_init)
                i = i + 1
        raise FileNotFoundError("There is not property file with name '" + file_name_init + "' in your project")

    path = property(get_property_file)


class log:
    val = True

    @property
    def to_do_info_logging(self):
        return self.val

    @to_do_info_logging.setter
    def set_value(self, value):
        self.val = value
    @to_do_info_logging.getter
    def get_value(self):
        return self.val


class JDISettings(object):

    JDI_SETTINGS_FILE_PATH = PropertyPath().get_property_file()

    __wait_element_sec = 20
    _driver_factory = None
    __logger = None
    _jdi_settings = None
    asserter = BaseMatcher()

    @staticmethod
    def get_driver_factory(): return JDISettings._driver_factory

    @staticmethod
    def _read_jdi_settings():
        if JDISettings._jdi_settings is None:
            f = open(JDISettings.JDI_SETTINGS_FILE_PATH)
            JDISettings._jdi_settings = dict()
            for line in f:
                param = line.split("=")
                JDISettings._jdi_settings[param[0]] = param[1].strip()

    @staticmethod
    def get_driver_path(): return JDISettings.get_setting_by_name("drivers_folder")

    @staticmethod
    def get_setting_by_name(setting_name):
        if JDISettings._jdi_settings is None or setting_name in JDISettings._jdi_settings:
            JDISettings._read_jdi_settings()
        return JDISettings._jdi_settings[setting_name] if setting_name in JDISettings._jdi_settings else None

    @staticmethod
    def get_current_timeout_sec():
        prop = JDISettings.get_setting_by_name("timeout_wait_element")
        return JDISettings.__wait_element_sec if prop is None else prop

    @staticmethod
    def get_domain():
       return JDISettings.get_setting_by_name("domain")

