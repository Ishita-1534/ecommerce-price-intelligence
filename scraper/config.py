"""
Project Configuration
"""

# Target E-Commerce Website
BASE_URL = "https://books.toscrape.com/"

# HTTP Request Headers
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

# Request Timeout (seconds)
REQUEST_TIMEOUT = 30