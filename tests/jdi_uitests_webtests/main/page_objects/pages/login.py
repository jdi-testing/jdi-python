from JDI.web.selenium.elements.api_interact.find_element_by import By
from JDI.web.selenium.elements.base.clickable import Clickable
from JDI.web.selenium.elements.common.button import Button
from JDI.web.selenium.elements.common.text_field import TextField
from JDI.web.selenium.elements.composite.form import Form


class Login(Form):

    login = TextField(By.id("name"))

    password = TextField(By.id("password"))

    button = Button(By.css(".btn-login"))

    profile = Clickable(By.css(".profile-photo"))

    def submit(self, user):
        Login.profile.click()
        super(Login, self).submit_form(user)
