from .config import conn, cursor

class Customer:
    def __init__(self, id, name, email, phone, address):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"<Customer {self.id} {self.name} {self.email} {self.phone} {self.address}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            address TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Customer table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS customers;"
        cursor.execute(sql)
        conn.commit()
        print("Customer table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO customers (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.email, self.phone, self.address))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, email, phone, address):
        customer = cls(None, name, email, phone, address)
        customer.save()
        return customer

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM customers WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        rows = cursor.fetchall()
        customers = [cls(*row) for row in rows]
        return customers

    def delete(self):
        sql = "DELETE FROM customers WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    def update(self, name=None, email=None, phone=None, address=None):
        self.name = name or self.name
        self.email = email or self.email
        self.phone = phone or self.phone
        self.address = address or self.address
        sql = """
            UPDATE customers
            SET name = ?, email = ?, phone = ?, address = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.email, self.phone, self.address, self.id))
        conn.commit()