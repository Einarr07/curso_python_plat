class Order:
    global_discount = 10
    min_amount = 300

    def __init__(self, amount):
        self.amount = amount

    def calculate_min_amount(self):
        if self.amount < self.min_amount:
            raise ValueError(f'You cannot do this transaction, the minimum amount is {self.min_amount}')
        else:
            self.amount -= self.global_discount

    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount


order_1 = Order(500)
order_1.update_global_discount(30)
order_1.calculate_min_amount()

print(f'This is the amount to be paid after the discount: {order_1.amount}')