from bs4 import BeautifulSoup
from models.product import Product


class ProductScraper:

    @staticmethod
    def extract_products(soup: BeautifulSoup):

        products = []

        books = soup.select("article.product_pod")

        for book in books:

            title = book.h3.a["title"]

            price = book.select_one(".price_color").text.replace("£", "")

            rating = book.p["class"][1]

            availability = book.select_one(".availability").text.strip()

            url = book.h3.a["href"]

            product = Product(
                product_name=title,
                price=price,
                rating=rating,
                availability=availability,
                product_url=url
            )

            products.append(product)

        return products