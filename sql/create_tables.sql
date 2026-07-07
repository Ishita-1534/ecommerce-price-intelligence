CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(500),
    price DECIMAL(10,2),
    rating VARCHAR(20),
    availability VARCHAR(100),
    product_url TEXT
);

SHOW COLUMNS FROM books;