
class Item:
    """Class used to represent a item"""

    def __init__(self, name: str, quantity: int, price: int):
        """
        :param name:
            Item name
        :param quantity:
            Purchase item units
        :param price:
            Price of each unit of the purchase item
        """

        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def multiplication(self) -> int:
        """
        Multiplies the quantity by the price of the purchase item

        :return:
            Result of multiplying the quantity by the price of the purchase item
        """

        return self.quantity * self.price
