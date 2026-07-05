from scraper.base_scraper import BaseScraper
from scraper.config import BASE_URL, SEARCH_KEYWORDS


def main():

    print("=" * 60)
    print("E-Commerce Price Intelligence Platform")
    print("=" * 60)

    scraper = BaseScraper()

    # For now, we'll test only the first keyword
    keyword = SEARCH_KEYWORDS[0]

    search_url = f"{BASE_URL}/sch/i.html?_nkw={keyword}"

    print(f"Searching for: {keyword}")

    html = scraper.get_page(search_url)

    print("HTML Downloaded Successfully")
    print(f"HTML Length: {len(html)}")

    scraper.close()


if __name__ == "__main__":
    main()