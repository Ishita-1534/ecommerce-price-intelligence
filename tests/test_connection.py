from scraper.base_scraper import BaseScraper


def main():
    scraper = BaseScraper()

    html = scraper.fetch_page("https://books.toscrape.com/")

    with open("data/raw/homepage.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("Connection Successful!")
    print(f"Downloaded {len(html)} characters.")
    print("HTML saved successfully.")


if __name__ == "__main__":
    main()