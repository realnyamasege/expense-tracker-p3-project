import datetime
from .database import create_connection

class Expense:
    def __init__(self, user_id, category_id, name, amount, description, date, is_recurring=False) -> None:
        self.user_id = user_id
        self.category_id = category_id
        self.name = name
        self.amount = amount
        self.description = description
        self.date = date
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        self.is_recurring = is_recurring

    def __repr__(self):
        return f"<Expense: {self.name}, ${self.amount:.2f}, Date: {self.date} >"

    @classmethod
    def add_expense(cls, user_id, category_id, name, amount, description, date, is_recurring=False):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO expenses (user_id, category_id, name, amount, description, date, created_at, updated_at, is_recurring) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                           (user_id, category_id, name, amount, description, date, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat(), is_recurring))
            conn.commit()

    @classmethod
    def get_expenses_by_user(cls, user_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
            return cursor.fetchall()

    @classmethod
    def update_expense(cls, expense_id, name=None, category_id=None, amount=None, description=None, date=None, is_recurring=None):
        with create_connection() as conn:
            cursor = conn.cursor()
            if name:
                cursor.execute("UPDATE expenses SET name = ?, updated_at = ? WHERE id = ?", (name, datetime.datetime.now().isoformat(), expense_id))
            if category_id:
                cursor.execute("UPDATE expenses SET category_id = ?, updated_at = ? WHERE id = ?", (category_id, datetime.datetime.now().isoformat(), expense_id))
            if amount is not None:
                cursor.execute("UPDATE expenses SET amount = ?, updated_at = ? WHERE id = ?", (amount, datetime.datetime.now().isoformat(), expense_id))
            if description:
                cursor.execute("UPDATE expenses SET description = ?, updated_at = ? WHERE id = ?", (description, datetime.datetime.now().isoformat(), expense_id))
            if date:
                cursor.execute("UPDATE expenses SET date = ?, updated_at = ? WHERE id = ?", (date, datetime.datetime.now().isoformat(), expense_id))
            if is_recurring is not None:
                cursor.execute("UPDATE expenses SET is_recurring = ?, updated_at = ? WHERE id = ?", (is_recurring, datetime.datetime.now().isoformat(), expense_id))
            conn.commit()

    @classmethod
    def delete_expense(cls, expense_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()

    @classmethod
    def count_expenses(cls, user_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM expenses WHERE user_id = ?", (user_id,))
            return cursor.fetchone()[0]

    @classmethod
    def get_expense_by_id(cls, expense_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
            return cursor.fetchone()

    @classmethod
    def get_expenses_by_date_range(cls, user_id, start_date, end_date):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE user_id = ? AND date BETWEEN ? AND ?", (user_id, start_date, end_date))
            return cursor.fetchall()

    @classmethod
    def get_total_amount_spent(cls, user_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id = ?", (user_id,))
            return cursor.fetchone()[0]
