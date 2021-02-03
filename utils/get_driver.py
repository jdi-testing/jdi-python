# TODO: get last chromedriver version
# TODO: get particular chromedriver version
# TODO: download chromedriver and save to path
# TODO: download and install chrome
# TODO: argparse
import requests
import zipfile

CHROMEDRIVER_URL = "https://chromedriver.storage.googleapis.com"


def download_driver(link, extract_path="."):
    filename = link.split("/")[-1]
    r = requests.get(link, stream=True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content():
            f.write(chunk)
    with zipfile.ZipFile(filename, "r") as zf:
        zf.extractall(path=extract_path)


def get_last_release(build=None) -> str:
    # TODO: if build is set get last version for this build
    if not build:
        r = requests.get(f"{CHROMEDRIVER_URL}/LATEST_RELEASE")
    else:
        r = requests.get(f"{CHROMEDRIVER_URL}/LATEST_RELEASE_{build}")
    return r.text


def compose_download_link(build) -> str:
    return f"{CHROMEDRIVER_URL}/{build}/chromedriver_win32.zip"


if __name__ == "__main__":
    release = get_last_release("87.0.4280")
    download_link = compose_download_link(build=release)
    download_driver(download_link)
