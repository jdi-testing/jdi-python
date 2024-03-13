from JDI.web.selenium.elements.api_interact.find_element_by import By
from JDI.web.selenium.elements.complex.table.table import Table
from JDI.web.selenium.elements.composite.web_page import WebPage


class SearchPage(WebPage):
    def __init__(self, url, title):
        super(SearchPage, self).__init__(url=url, title=title)

    # TODO: Implement SearchPage
