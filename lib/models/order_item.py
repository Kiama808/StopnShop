from .config import conn, cursor

class OrderItem:
    def __init__(self, id, order_id, product_id, quantity, price):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"<OrderItem {self.id} {self.order_id} {self.product_id} {self.quantity} {self.price}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("OrderItem table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS order_items;"
        cursor.execute(sql)
        conn.commit()
        print("OrderItem table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.order_id, self.product_id, self.quantity, self.price))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, order_id, product_id, quantity, price):
        order_item = cls(None, order_id, product_id, quantity, price)
        order_item.save()
        return order_item

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM order_items WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM order_items"
        cursor.execute(sql)
        rows = cursor.fetchall()
        order_items = [cls(*row) for row in rows]
        return order_items

    def delete(self):
        sql = "DELETE FROM order_items WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    def update(self, order_id=None, product_id=None, quantity=None, price=None):
        self.order_id = order_id or self.order_id
        self.product_id = product_id or self.product_id
        self.quantity = quantity if quantity is not None else self.quantity
        self.price = price if price is not None else self.price
        sql = """
            UPDATE order_items
            SET order_id = ?, product_id = ?, quantity = ?, price = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.order_id, self.product_id, self.quantity, self.price, self.id))
        conn.commit()