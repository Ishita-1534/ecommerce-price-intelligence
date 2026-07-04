from dataclasses import dataclass

@dataclass
class Product:
    product_id: str
    product_name: str
    brand: str
    category: str
    price: float
    original_price: float
    discount: float
    rating: float
    review_count: int
    availability: str
    product_url: str
    image_url: str
    date_collected: str