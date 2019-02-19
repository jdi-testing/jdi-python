from JDI.core.interfaces.application import Application
from JDI.web.selenium.elements.web_cascade_init import WebCascadeInit
from JDI.web.selenium.settings.web_settings import WebSettings


class WebSite(Application):

    @staticmethod
    def _init(site):
        WebCascadeInit().init_site_page(site)

    @staticmethod
    def init(site):
        WebSettings.use_driver()
        WebCascadeInit().init_site_page(site)
