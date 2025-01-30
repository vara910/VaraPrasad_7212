class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_details(self):
        return f"{self.first_name} {self.last_name}"

class Customer(Person):
    def __init__(self, first_name, last_name, customer_id):
        super().__init__(first_name, last_name)
        self.customer_id = customer_id

    def display_details(self):
        return f"Customer ID: {self.customer_id}, {super().display_details()}"

class Order(Customer):
    def __init__(self, first_name, last_name, customer_id, order_id, order_status, order_date):
        super().__init__(first_name, last_name, customer_id)
        self.order_id = order_id
        self.order_status = order_status
        self.order_date = order_date

    def display_order_details(self):
        return f"{super().display_details()}, Order ID: {self.order_id}, Status: {self.order_status}, Order Date: {self.order_date}"

class OrderItem(Order):
    def __init__(self, first_name, last_name, customer_id, order_id, order_status, order_date, item_id, product_id, quantity):
        super().__init__(first_name, last_name, customer_id, order_id, order_status, order_date)
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity

    def display_item_details(self):
        return f"{super().display_order_details()}, Item ID: {self.item_id}, Product ID: {self.product_id}, Quantity: {self.quantity}"

customer = Customer("John", "Doe", 1001)
order = Order("John", "Doe", 1001, 1, "Shipped", "2023-09-25")
order_item = OrderItem("John", "Doe", 1001, 1, "Shipped", "2023-09-25", 1, 301, 2)

print(customer.display_details())
print(order.display_order_details())
print(order_item.display_item_details())
