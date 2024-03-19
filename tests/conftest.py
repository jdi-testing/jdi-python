
# conftest.py
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type of browser: chrome or firefox")

