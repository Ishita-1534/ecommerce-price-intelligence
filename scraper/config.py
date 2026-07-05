"""
Project Configuration
"""

BASE_URL = "https://www.ebay.com"

SEARCH_KEYWORDS = [
    "laptop",
    "mobile",
    "headphones",
    "watch",
    "camera",
    "tablet",
    "keyboard",
    "mouse",
    "speaker",
    "monitor"
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}

REQUEST_TIMEOUT = 30
