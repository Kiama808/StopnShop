import sys
from datetime import datetime
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_item import OrderItem

def main():
    while True:
        print("\nWelcome To StopnShop:")
        print("1. Product Management")
        print("2. Customer Management")
        print("3. Order Management")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            product_management()
        elif choice == "2":
            customer_management()
        elif choice == "3":
            order_management()
        elif choice == "4":
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def product_management():
    while True:
        print("\nProduct Management:")
        print("1. List all products")
        print("2. Create a new product")
        print("3. Update an existing product")
        print("4. Delete a product")
        print("5. Exit to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            list_products()
        elif choice == "2":
            create_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def list_products():
    products = Product.select()
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Description: {product.description}, Price: {product.price}, Quantity: {product.quantity}")

def create_product():
    name = input("Enter product name: ")
    description = input("Enter product description:")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    Product.create(name, description, price, quantity)
    print("Product created successfully.")

def update_product():
    product_id = int(input("Enter the product ID to update: "))
    product = Product.find_by_id(product_id)
    if product:
        name = input(f"Enter new name ({product.name}): ") or product.name
        description = input(f"Enter new description ({product.description}): ") or product.description
        price = input(f"Enter new price ({product.price}): ")
        price = float(price) if price else product.price
        quantity = input(f"Enter new quantity ({product.quantity}): ")
        quantity = int(quantity) if quantity else product.quantity
        product.update(name=name, description=description, price=price, quantity=quantity)
        print("Product updated successfully.")
    else:
        print("Product not found.")

def delete_product():
    product_id = int(input("Enter the product ID to delete: "))
    product = Product.find_by_id(product_id)
    if product:
        product.delete()
        print("Product deleted successfully.")
    else:
        print("Product not found.")

def customer_management():
    while True:
        print("\nCustomer Management:")
        print("1. List all customers")
        print("2. Create a new customer")
        print("3. Update an existing customer")
        print("4. Delete a customer")
        print("5. Exit to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            list_customers()
        elif choice == "2":
            create_customer()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def list_customers():
    customers = Customer.select()
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}, Address: {customer.address}")

def create_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")
    Customer.create(name, email, phone, address)
    print("Customer created successfully.")

def update_customer():
    customer_id = int(input("Enter the customer ID to update: "))
    customer = Customer.find_by_id(customer_id)
    if customer:
        name = input(f"Enter new name ({customer.name}): ") or customer.name
        email = input(f"Enter new email ({customer.email}): ") or customer.email
        phone = input(f"Enter new phone ({customer.phone}): ") or customer.phone
        address = input(f"Enter new address ({customer.address}): ") or customer.address
        customer.update(name=name, email=email, phone=phone, address=address)
        print("Customer updated successfully.")
    else:
        print("Customer not found.")

def delete_customer():
    customer_id = int(input("Enter the customer ID to delete: "))
    customer = Customer.find_by_id(customer_id)
    if customer:
        customer.delete()
        print("Customer deleted successfully.")
    else:
        print("Customer not found.")

def order_management():
    while True:
        print("\nOrder Management:")
        print("1. List all orders")
        print("2. Create a new order")
        print("3. Update an existing order")
        print("4. Delete an order")
        print("5. Search for orders by customer ID")
        print("6. Exit to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            list_orders()
        elif choice == "2":
            create_order()
        elif choice == "3":
            update_order()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            search_order()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def list_orders():
    orders = Order.select()
    for order in orders:
        print(f"ID: {order.id}, Customer ID: {order.customer_id}, Order Date: {order.order_date}, Status: {order.status}")

def create_order():
    customer_id = int(input("Enter customer ID: "))
    order_date = input("Enter order date (YYYY-MM-DD): ")
    status = input("Enter order status: ")
    order = Order.create(customer_id, order_date, status)
    print("Order created successfully.")
    manage_order_items(order.id)

def update_order():
    order_id = int(input("Enter the order ID to update: "))
    order = Order.find_by_id(order_id)
    if order:
        customer_id = input(f"Enter new customer ID ({order.customer_id}): ")
        customer_id = int(customer_id) if customer_id else order.customer_id
        order_date = input(f"Enter new order date ({order.order_date}): ") or order.order_date
        status = input(f"Enter new status ({order.status}): ") or order.status
        order.update(customer_id=customer_id, order_date=order_date, status=status)
        print("Order updated successfully.")
    else:
        print("Order not found.")

def delete_order():
    order_id = int(input("Enter the order ID to delete: "))
    order = Order.find_by_id(order_id)
    if order:
        order.delete()
        print("Order deleted successfully.")
    else:
        print("Order not found.")

def search_order():
    customer_id = int(input("Enter the Customer ID to search for orders: "))
    orders = Order.find_by_customer_id(customer_id)
    if orders:
        for order in orders:
            print(f"ID: {order.id}, Customer ID: {order.customer_id}, Order Date: {order.order_date}, Status: {order.status}")
    else:
        print("No orders found for that customer.")

def manage_order_items(order_id):
    while True:
        print(f"\nManaging items for Order ID: {order_id}")
        print("1. List all order items")
        print("2. Add an order item")
        print("3. Update an order item")
        print("4. Delete an order item")
        print("5. Exit to order management")

        choice = input("Enter choice: ")

        if choice == "1":
            list_order_items(order_id)
        elif choice == "2":
            add_order_item(order_id)
        elif choice == "3":
            update_order_item(order_id)
        elif choice == "4":
            delete_order_item(order_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def list_order_items(order_id):
    order_items = OrderItem.select()
    for item in order_items:
        if item.order_id == order_id:
            print(f"ID: {item.id}, Order ID: {item.order_id}, Product ID: {item.product_id}, Quantity: {item.quantity}, Price: {item.price}")

def add_order_item(order_id):
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    OrderItem.create(order_id, product_id, quantity, price)
    print("Order item added successfully.")

def update_order_item(order_id):
    item_id = int(input("Enter the order item ID to update: "))
    item = OrderItem.find_by_id(item_id)
    if item and item.order_id == order_id:
        product_id = input(f"Enter new product ID ({item.product_id}): ")
        product_id = int(product_id) if product_id else item.product_id
        quantity = input(f"Enter new quantity ({item.quantity}): ")
        quantity = int(quantity) if quantity else item.quantity
        price = input(f"Enter new price ({item.price}): ")
        price = float(price) if price else item.price
        item.update(product_id=product_id, quantity=quantity, price=price)
        print("Order item updated successfully.")
    else:
        print("Order item not found or does not belong to the current order.")

def delete_order_item(order_id):
    item_id = int(input("Enter the order item ID to delete: "))
    item = OrderItem.find_by_id(item_id)
    if item and item.order_id == order_id:
        item.delete()
        print("Order item deleted successfully.")
    else:
        print("Order item not found or does not belong to the current order.")

if __name__ == "__main__":
    main()