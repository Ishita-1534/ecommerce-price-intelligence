import requests


class BaseScraper:
    """
    Base class for all web scrapers.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            )
        }

    def get_page(self, url):
        """
        Download the HTML of a webpage.
        """

        response = requests.get(url, headers=self.headers, timeout=20)

        response.raise_for_status()

        return response.text