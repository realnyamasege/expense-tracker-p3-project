import datetime
from .database import create_connection

class User:
    def __init__(self, username, password, email, budget) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.budget = budget
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        self.is_active = True

    def __repr__(self):
        return f"<User: {self.username}, Budget: ${self.budget:.2f} >"

    @classmethod
    def create_user(cls, username, password, email, budget):
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO users (username, password, email, budget, created_at, updated_at, is_active) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, 
                (username, password, email, budget, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat(), 1))
                conn.commit()
            print(f"User {username} created successfully.")
        except Exception as e:
            print(f"Error creating user: {e}")

    @classmethod
    def get_user(cls, username):
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
                user = cursor.fetchone()
            if user:
                return user
            else:
                print(f"No user found with username: {username}")
                return None
        except Exception as e:
            print(f"Error retrieving user: {e}")

    @classmethod
    def update_user(cls, username, password=None, email=None, budget=None, is_active=None):
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                if password:
                    cursor.execute("UPDATE users SET password = ?, updated_at = ? WHERE username = ?", (password, datetime.datetime.now().isoformat(), username))
                if email:
                    cursor.execute("UPDATE users SET email = ?, updated_at = ? WHERE username = ?", (email, datetime.datetime.now().isoformat(), username))
                if budget is not None:
                    cursor.execute("UPDATE users SET budget = ?, updated_at = ? WHERE username = ?", (budget, datetime.datetime.now().isoformat(), username))
                if is_active is not None:
                    cursor.execute("UPDATE users SET is_active = ?, updated_at = ? WHERE username = ?", (is_active, datetime.datetime.now().isoformat(), username))
                conn.commit()
            print(f"User {username} updated successfully.")
        except Exception as e:
            print(f"Error updating user: {e}")

    @classmethod
    def delete_user(cls, username):
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM users WHERE username = ?", (username,))
                conn.commit()
            print(f"User {username} deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {e}")

    @classmethod
    def get_all_users(cls):
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
            if users:
                return users
            else:
                print("No users found.")
                return []
        except Exception as e:
            print(f"Error retrieving users: {e}")

    @classmethod
    def get_user_by_id(cls, user_id):
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
                user = cursor.fetchone()
            if user:
                return user
            else:
                print(f"No user found with ID: {user_id}")
                return None
        except Exception as e:
            print(f"Error retrieving user by ID: {e}")
