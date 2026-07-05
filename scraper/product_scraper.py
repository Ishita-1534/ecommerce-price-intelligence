from models.product import Product


class ProductScraper:

    @staticmethod
    def extract_products(soup):

        products = []

        cards = soup.find_all("article", class_="product_pod")

        for card in cards:

            name = card.h3.a["title"]

            price = (
            card.find("p", class_="price_color")
            .text.strip()
           .replace("Â", "")
)

            rating = card.find("p", class_="star-rating")["class"][1]

            availability = (
                card.find("p", class_="instock availability")
                .text.strip()
            )

            product_url = card.h3.a["href"]

            product = Product(
                name,
                price,
                rating,
                availability,
                product_url,
            )

            products.append(product)

        return products