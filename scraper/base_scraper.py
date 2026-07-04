import requests

class BaseScraper:

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        }

    def get_page(self, url):
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=30
            )

            response.raise_for_status()

            return response.text

        except requests.RequestException as e:
            print(f"Error: {e}")
            return None