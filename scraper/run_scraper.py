from database.insert_books import BookDatabase
from scraper.base_scraper import BaseScraper
from scraper.html_parser import HTMLParser
from scraper.product_scraper import ProductScraper
from etl.csv_writer import CSVWriter
from scraper.config import BASE_URL, TOTAL_PAGES


def main():

    scraper = BaseScraper()

    all_products = []

    for page in range(1, TOTAL_PAGES + 1):

        if page == 1:
            url = BASE_URL
        else:
            url = BASE_URL + f"catalogue/page-{page}.html"

        print(f"Scraping Page {page}...")

        html = scraper.get_page(url)

        soup = HTMLParser.parse(html)

        products = ProductScraper.extract_products(soup)

        print(f"Found {len(products)} products")

        all_products.extend(products)

    scraper.close()

    CSVWriter.save(
        all_products,
        "data/raw/products.csv"
    )
    BookDatabase.insert_books(all_products)

    print("=" * 50)
    print(f"Total Products : {len(all_products)}")
    print("=" * 50)


if __name__ == "__main__":
    main()