from __future__ import with_statement

import json
import logging
import logging.config
from io import open

from JDI.core.settings.jdi_settings import PropertyPath


class JDILogger(object):
    JDI_LOGGING_CONFIG_FILE_PATH = PropertyPath("logging.json").get_property_file()

    def __init__(self, name="JDI Logger"):

        with open(self.JDI_LOGGING_CONFIG_FILE_PATH, 'r') as fd:
            logging.config.dictConfig(json.load(fd))
        self.logger = logging.getLogger(name)

    def __getattr__(self, name):
        return getattr(self.logger, name)
