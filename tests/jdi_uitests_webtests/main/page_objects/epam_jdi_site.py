from JDI.web.selenium.elements.api_interact.find_element_by import By
from JDI.web.selenium.elements.complex.text_list import TextList
from JDI.web.selenium.elements.composite.web_site import WebSite
from tests.jdi_uitests_webtests.main.enums.preconditions import Preconditions
from tests.jdi_uitests_webtests.main.page_objects.pages import (
    ContactFormPage,
    DatesPage,
    HomePage,
    Login,
    MetalColorPage,
    SupportPage,
)
from tests.jdi_uitests_webtests.main.page_objects.pages.simple_table_page import SimpleTablePage
from tests.jdi_uitests_webtests.main.page_objects.sections.footer import Footer
from tests.jdi_uitests_webtests.main.page_objects.sections.header import Header


class EpamJDISite(WebSite):
    # pages
    home_page = HomePage(url=Preconditions.HOME_PAGE.value, title="Index Page")
    metals_colors_page = MetalColorPage(url=Preconditions.METALS_AND_COLORS_PAGE.value,
                                        title="Metal and Colors")
    contact_form_page = ContactFormPage(url=Preconditions.CONTACT_PAGE.value,
                                        title="Contact Form")
    support_page = SupportPage(url=Preconditions.SUPPORT_PAGE.value, title="Support")
    dates_page = DatesPage(url=Preconditions.DATES_PAGE.value, title="Simple Table")
    simple_table_page = SimpleTablePage(url=Preconditions.SIMPLE_TABLE_PAGE.value,
                                        title="Simple Table")

    # elements
    actions_log = TextList(By.css(".logs li"))

    # sections
    footer = Footer(By.css(".footer-content"))
    login_page = Login(By.css(".uui-profile-menu"))
    header = Header(By.css(".uui-header"))
