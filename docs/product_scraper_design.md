# Product Scraper Design

## Objective

Collect product information from an e-commerce website.

## Workflow

1. Open homepage/category page.
2. Find product links.
3. Visit each product page.
4. Extract product information.
5. Store the extracted data.
6. Save raw data for ETL processing.

## Product Fields

- Product ID
- Product Name
- Brand
- Category
- Price
- Original Price
- Discount
- Rating
- Review Count
- Availability
- Product URL
- Image URL
- Date Collected

## Output

CSV file in:
data/raw/