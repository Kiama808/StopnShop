from models.customer import Customer
from models.product import Product
from models.order import Order
from models.order_item import OrderItem

# Create tables
Customer.create_table()
Product.create_table()
Order.create_table()
OrderItem.create_table()

print("Tables created successfully.")