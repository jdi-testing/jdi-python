import logging
import time

try:
    import win32com.client
except ModuleNotFoundError as e:
    logging.exception(e)


class jdi_win32:
    @staticmethod
    def paste_text(text):
        shell = win32com.client.Dispatch("WScript.Shell")

        time.sleep(3)
        shell.Sendkeys(text)
        shell.Sendkeys("~")
