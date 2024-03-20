from JDI.core.settings.jdi_settings import JDISettings


class User:
    @staticmethod
    def default():
        return User()

    def __init__(self):
        self.login = JDISettings.get_setting_by_name("user")
        self.password = JDISettings.get_setting_by_name("password")
