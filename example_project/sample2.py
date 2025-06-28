def calculate_discount(price, discount):
    """
    Calculate discounted price given a percentage.
    """
    return price * (1 - discount / 100)

class Product:
    """
    Represents a product with pricing and stock.
    """

    def __init__(self, name, price, stock):
        """
        Initialize a Product instance.
        """
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        """
        Check if the product is in stock.
        """
        return self.stock > 0
