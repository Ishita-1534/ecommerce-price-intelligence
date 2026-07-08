# Scraper Architecture

## Modules

### BaseScraper
- Initializes the Selenium WebDriver
- Opens web pages
- Retrieves HTML source
- Closes the browser

### HTMLParser
- Parses HTML using BeautifulSoup

### ProductScraper
- Extracts book information from each page
- Creates `Product` objects

### CSVWriter
- Saves scraped data to a CSV file

### BookDatabase
- Inserts scraped data into the MySQL database

## Workflow

1. Open webpage using Selenium.
2. Download HTML source.
3. Parse HTML with BeautifulSoup.
4. Extract book information.
5. Save data to CSV.
6. Store data in MySQL.

## Status

Completed