import time

import win32com.client


class jdi_win32:
    @staticmethod
    def paste_text(text):
        shell = win32com.client.Dispatch("WScript.Shell")

        time.sleep(3)
        shell.Sendkeys(text)
        shell.Sendkeys("~") 
