from database.db_connection import get_connection


class BookDatabase:

    @staticmethod
    def insert_books(products):

        # Connect to MySQL
        connection = get_connection()
        cursor = connection.cursor()

        # Delete old data to avoid duplicates
        cursor.execute("TRUNCATE TABLE books")

        # SQL Query
        sql = """
        INSERT INTO books
        (
            product_name,
            price,
            rating,
            availability,
            product_url
        )
        VALUES
        (%s, %s, %s, %s, %s)
        """

        # Prepare data
        values = []

        for product in products:

            values.append(
                (
                    product.product_name,
                    float(product.price),
                    product.rating,
                    product.availability,
                    product.product_url
                )
            )

        # Insert all books
        cursor.executemany(sql, values)

        # Save changes
        connection.commit()

        print("=" * 50)
        print(f"{cursor.rowcount} Books Inserted Successfully")
        print("=" * 50)

        # Close connection
        cursor.close()
        connection.close()