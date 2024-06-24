from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def get_chromedriver() -> WebDriver:
    script_directory = Path(__file__).resolve().parent
    driver_path = script_directory.joinpath("chromedriver-mac-arm64", "chromedriver")
    service = Service(str(driver_path))
    return webdriver.Chrome(service=service)


def main():
    driver = get_chromedriver()
    driver.get("https://my.raceresult.com/192607")
    driver.quit()


if __name__ == "__main__":
    main()
