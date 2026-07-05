from scraper.base_scraper import BaseScraper
from scraper.file_manager import FileManager
from scraper.config import BASE_URL
from scraper.html_parser import HTMLParser
from scraper.product_scraper import ProductScraper
from etl.csv_writer import CSVWriter


def main():
    print("=" * 60)
    print("E-Commerce Price Intelligence & Competitive Analytics Platform")
    print("=" * 60)
    print("Starting scraper...\n")

    # Initialize scraper
    scraper = BaseScraper()

    # Download HTML
    html = scraper.get_page(BASE_URL)

    if html:
        print("✅ Page downloaded successfully!")
        print(f"📄 HTML Length: {len(html)} characters")

        # Save raw HTML
        FileManager.save_html(html, "data/raw/homepage.html")
        print("✅ HTML saved successfully.")

        # Parse HTML
        soup = HTMLParser.parse(html)

        # Extract products
        products = ProductScraper.extract_products(soup)

        print(f"\n📦 Products Found: {len(products)}\n")

        # Display products
        for i, product in enumerate(products, start=1):
            print(f"Product {i}")
            print("-" * 40)
            print(product.to_dict())
            print()

        # Save products to CSV
        CSVWriter.save(products, "data/raw/products.csv")

        print("\n✅ Scraping completed successfully!")

    else:
        print("❌ Failed to download page.")


if __name__ == "__main__":
    main()