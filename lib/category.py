from .database import create_connection

class Category:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Category: {self.name} >"

    @classmethod
    def create_category(cls, name, description):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categories (name, description) VALUES (?, ?)", (name, description))
            conn.commit()

    @classmethod
    def get_all_categories(cls):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categories")
            return cursor.fetchall()
