# Database Design

## Database

**book_price_intelligence**

## Tables

### 1. books

| Column | Data Type |
|---------|-----------|
| id | INT (Primary Key, Auto Increment) |
| product_name | VARCHAR(500) |
| price | DECIMAL(10,2) |
| rating | VARCHAR(20) |
| availability | VARCHAR(100) |
| product_url | TEXT |

## Relationships

This project currently uses a single table (`books`) since all required information is available within each scraped record.

## Status

Completed