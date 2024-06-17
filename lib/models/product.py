from .config import conn, cursor

class Product:
    def __init__(self, id, name, description, price, quantity):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"<Product {self.id} {self.name} {self.description} {self.price} {self.quantity}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Product table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS products;"
        cursor.execute(sql)
        conn.commit()
        print("Product table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO products (name, description, price, quantity)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.price, self.quantity))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, description, price, quantity):
        product = cls(None, name, description, price, quantity)
        product.save()
        return product

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM products WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        rows = cursor.fetchall()
        products = [cls(*row) for row in rows]
        return products

    def delete(self):
        sql = "DELETE FROM products WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    def update(self, name=None, description=None, price=None, quantity=None):
        self.name = name or self.name
        self.description = description or self.description
        self.price = price if price is not None else self.price
        self.quantity = quantity if quantity is not None else self.quantity
        sql = """
            UPDATE products
            SET name = ?, description = ?, price = ?, quantity = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.description, self.price, self.quantity, self.id))
        conn.commit()