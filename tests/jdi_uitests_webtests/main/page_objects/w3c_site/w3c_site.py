from JDI.web.selenium.elements.composite.web_site import WebSite
from tests.jdi_uitests_webtests.main.page_objects.w3c_site.frame_page import FramePage


class W3cSite(WebSite):
    domain = "https://www.w3schools.com"

    frame_page = FramePage(url="/tags/tag_button.asp", domain=domain)
