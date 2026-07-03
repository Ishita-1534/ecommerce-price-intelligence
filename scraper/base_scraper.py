"""
Base Scraper

Handles HTTP requests for the project.
"""

import requests

from scraper.config import BASE_URL, HEADERS, REQUEST_TIMEOUT


class BaseScraper:
    """Base class responsible for downloading web pages."""

    def fetch_page(self, url: str) -> str:
        """Download a webpage and return its HTML."""

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        return response.text