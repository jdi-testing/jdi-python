from enum import Enum
from abc import ABCMeta, abstractmethod
from JDI.web.selenium.elements.api_interact.find_element_by import By
from JDI.web.selenium.elements.complex.radio_buttons import RadioButtons
from JDI.web.selenium.elements.complex.selector import Selector
from JDI.web.selenium.elements.composite.section import Section

ERROR_MSG = "No elements selected. Override getSelectedAction or place locator to <select> tag"


class SelectElements(metaclass=ABCMeta):
    @abstractmethod
    def get_input_web_elements(self):
        raise NotImplementedError

    def get_selected(self):
        element = list(filter(lambda x: x.is_selected(), self.get_input_web_elements()))
        if len(element) == 0:
            raise ValueError(ERROR_MSG)
        return element[0].find_element_by_xpath("..").text

    def is_selected_action(self, element) -> bool:
        actual_text = (
            list(filter(lambda x: x.is_selected(), self.get_input_web_elements()))[0].find_element_by_xpath("..").text
        )
        if isinstance(element, str):
            return actual_text == element
        elif isinstance(element, Enum):
            return actual_text == element.value
        return False

    def get_selected_index(self):
        try:
            return list(map(lambda x: x.is_selected(), self.get_input_web_elements())).index(True)
        except ValueError:
            raise ValueError(ERROR_MSG) from None


class RadioButtonsSummary(SelectElements, RadioButtons):
    def get_input_web_elements(self):
        return list(
            map(lambda el: el.find_element_by_tag_name("input"), super(RadioButtonsSummary, self).get_web_elements())
        )


class SelectorSummary(SelectElements, Selector):
    def get_input_web_elements(self):
        return list(
            map(lambda el: el.find_element_by_tag_name("input"), super(SelectorSummary, self).get_web_elements())
        )


class Summary(Section):
    odds_radio_buttons = RadioButtonsSummary(By.css("#odds-selector p"))

    odds_selector = SelectorSummary(By.css("#odds-selector p"))
