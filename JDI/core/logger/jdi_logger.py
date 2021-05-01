import json
import logging
import logging.config

from JDI.core.settings.jdi_settings import PropertyPath


class JDILogger:
    def __init__(self, filename="logging.json"):
        self.config_filename = PropertyPath(filename).get_property_file()
        with open(self.config_filename, "r") as fd:
            logging.config.dictConfig(json.load(fd))
        self.logger = logging.getLogger(__name__)

    def __getattr__(self, name):
        return getattr(self.logger, name)
