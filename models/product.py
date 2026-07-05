class Product:

    def __init__(
        self,
        search_keyword,
        product_name,
        price,
        shipping,
        condition,
        product_url,
        image_url
    ):
        self.search_keyword = search_keyword
        self.product_name = product_name
        self.price = price
        self.shipping = shipping
        self.condition = condition
        self.product_url = product_url
        self.image_url = image_url

    def to_dict(self):
        return {
            "Search Keyword": self.search_keyword,
            "Product Name": self.product_name,
            "Price": self.price,
            "Shipping": self.shipping,
            "Condition": self.condition,
            "Product URL": self.product_url,
            "Image URL": self.image_url
        }