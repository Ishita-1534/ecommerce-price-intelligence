from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


class BaseScraper:

    def __init__(self):

        options = Options()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def get_page(self, url):

        self.driver.get(url)

        time.sleep(5)

        return self.driver.page_source

    def close(self):

        self.driver.quit()