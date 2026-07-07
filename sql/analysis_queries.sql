USE book_price_intelligence;

-- ==========================================
-- BOOK PRICE INTELLIGENCE ANALYSIS
-- ==========================================

-- 1. Total Books
SELECT COUNT(*) AS Total_Books
FROM books;

-- 2. Average Price
SELECT ROUND(AVG(price),2) AS Average_Price
FROM books;

-- 3. Maximum Price
SELECT MAX(price) AS Maximum_Price
FROM books;

-- 4. Minimum Price
SELECT MIN(price) AS Minimum_Price
FROM books;

-- 5. Most Expensive Book
SELECT product_name,
       price,
       rating
FROM books
ORDER BY price DESC
LIMIT 1;

-- 6. Cheapest Book
SELECT product_name,
       price,
       rating
FROM books
ORDER BY price ASC
LIMIT 1;

-- 7. Rating Distribution
SELECT rating,
       COUNT(*) AS Total_Books
FROM books
GROUP BY rating
ORDER BY rating;

-- 8. Availability Distribution
SELECT availability,
       COUNT(*) AS Total_Books
FROM books
GROUP BY availability;

-- 9. Top 10 Most Expensive Books
SELECT product_name,
       price
FROM books
ORDER BY price DESC
LIMIT 10;

-- 10. Top 10 Cheapest Books
SELECT product_name,
       price
FROM books
ORDER BY price ASC
LIMIT 10;

-- 11. Average Price by Rating
SELECT rating,
       ROUND(AVG(price),2) AS Average_Price
FROM books
GROUP BY rating
ORDER BY rating;

-- 12. Price Category
SELECT
CASE
WHEN price < 20 THEN 'Cheap'
WHEN price BETWEEN 20 AND 40 THEN 'Medium'
ELSE 'Expensive'
END AS Price_Category,
COUNT(*) AS Total_Books
FROM books
GROUP BY Price_Category;

-- 13. Books Above Average Price
SELECT product_name,
       price
FROM books
WHERE price >
(
SELECT AVG(price)
FROM books
);

-- 14. Five-Star Books
SELECT product_name,
       price
FROM books
WHERE rating='Five'
ORDER BY price DESC;

-- 15. Books Currently In Stock
SELECT COUNT(*) AS In_Stock
FROM books
WHERE availability LIKE '%In stock%';

-- 16. Price Range
SELECT
MAX(price)-MIN(price) AS Price_Range
FROM books;

-- 17. Percentage of Books by Rating
SELECT
rating,
COUNT(*) AS Total_Books,
ROUND(
COUNT(*)*100/(SELECT COUNT(*) FROM books),2
) AS Percentage
FROM books
GROUP BY rating;

-- 18. Books Between £20 and £40
SELECT product_name,
       price
FROM books
WHERE price BETWEEN 20 AND 40;

-- 19. Average Price of Five-Star Books
SELECT ROUND(AVG(price),2) AS Five_Star_Average
FROM books
WHERE rating='Five';

-- 20. Total Number of Rating Categories
SELECT COUNT(DISTINCT rating) AS Rating_Categories
FROM books;