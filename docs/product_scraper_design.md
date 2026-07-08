# Product Scraper Design

## Objective

Extract book information from the **Books to Scrape** website for price analysis and business intelligence.

## Workflow

1. Open the target page using Selenium.
2. Retrieve the HTML source.
3. Parse the HTML using BeautifulSoup.
4. Locate all book containers.
5. Extract book information.
6. Store the extracted data as `Product` objects.
7. Export the data to a CSV file.
8. Insert the data into a MySQL database.

## Extracted Fields

- Book Name
- Price
- Rating
- Availability
- Product URL

## Output

- CSV File: `data/raw/products.csv`
- MySQL Table: `books`

## Status

Completed