from collections import namedtuple

Product = namedtuple("Product", ('name', 'price', 'quantity'),
                     defaults=(1,))

class order:
    def __init__(self):
        self._items = []
        self._status = "open"

    @property
    def status(self):
        return self.status

    @property
    def items(self):
        return self._items.copy()

    @property
    def total_price(self):
        return sum([price * quantity for _, price, quantity in self.items])

    def add_item(self, name: str, price: float, quantity: int = 1):
        self.items.append(Product(name, price, quantity))

    def update_status(self, status: str):
        status = status.lower()
        if status not in ('open', 'payed'):
            raise ValueError(f'Status may be "open" or "payed", got {status}')

        self.status = status