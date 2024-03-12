import os
from pathlib import Path

import pytest

from JDI.core.settings.jdi_settings import PropertyPath


@pytest.mark.unit
class TestPropertyPath:
    def test_creation_default(self):
        assert PropertyPath() is not PropertyPath()

    def test_creation_with_param(self):
        p = PropertyPath("test.txt")
        assert p._filename.name == "test.txt"

    @pytest.mark.skipif(os.getcwd() == os.path.dirname(__file__), reason="Tests require current directory to be the same as the test directory")
    def test_get_property_file(self):
        assert PropertyPath().get_property_file() == Path("jdi.properties").absolute()
