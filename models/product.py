class Product:

    def __init__(
        self,
        product_name,
        price,
        rating,
        availability,
        product_url
    ):

        self.product_name = product_name
        self.price = price
        self.rating = rating
        self.availability = availability
        self.product_url = product_url

    def to_dict(self):

        return {
            "Product Name": self.product_name,
            "Price": self.price,
            "Rating": self.rating,
            "Availability": self.availability,
            "Product URL": self.product_url
        }