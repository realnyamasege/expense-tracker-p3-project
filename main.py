from lib.database import init_db
from lib.user import User
from lib.expense import Expense
from lib.category import Category

def main():
    init_db()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Create User")
        print("2. Get User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Get All Users")
        print("6. Add Expense")
        print("7. Get Expenses by User")
        print("8. Update Expense")
        print("9. Delete Expense")
        print("10. Count Expenses")
        print("11. Get Expense by ID")
        print("12. Get Expenses by Date Range")
        print("13. Get Total Amount Spent")
        print("14. Create Category")
        print("15. Get All Categories")
        print("16. Exit")

        choice = input("\nEnter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            budget = float(input("Enter budget: "))
            User.create_user(username, password, email, budget)
        elif choice == '2':
            username = input("Enter username: ")
            print(User.get_user(username))
        elif choice == '3':
            username = input("Enter username: ")
            password = input("Enter new password (or leave blank to skip): ")
            email = input("Enter new email (or leave blank to skip): ")
            budget = input("Enter new budget (or leave blank to skip): ")
            is_active = input("Enter new active status (True/False or leave blank to skip): ")
            User.update_user(username, password or None, email or None, float(budget) if budget else None, bool(is_active) if is_active else None)
        elif choice == '4':
            username = input("Enter username: ")
            User.delete_user(username)
        elif choice == '5':
            print(User.get_all_users())
        elif choice == '6':
            user_id = int(input("Enter user ID: "))
            category_id = int(input("Enter category ID: "))
            name = input("Enter expense name: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            is_recurring = input("Is it a recurring expense? (True/False): ")
            Expense.add_expense(user_id, category_id, name, amount, description, date, bool(is_recurring))
        elif choice == '7':
            user_id = int(input("Enter user ID: "))
            print(Expense.get_expenses_by_user(user_id))
        elif choice == '8':
            expense_id = int(input("Enter expense ID: "))
            name = input("Enter new name (or leave blank to skip): ")
            category_id = input("Enter new category ID (or leave blank to skip): ")
            amount = input("Enter new amount (or leave blank to skip): ")
            description = input("Enter new description (or leave blank to skip): ")
            date = input("Enter new date (YYYY-MM-DD) (or leave blank to skip): ")
            is_recurring = input("Enter new recurring status (True/False or leave blank to skip): ")
            Expense.update_expense(expense_id, name or None, int(category_id) if category_id else None, float(amount) if amount else None, description or None, date or None, bool(is_recurring) if is_recurring else None)
        elif choice == '9':
            expense_id = int(input("Enter expense ID: "))
            Expense.delete_expense(expense_id)
        elif choice == '10':
            user_id = int(input("Enter user ID: "))
            print(Expense.count_expenses(user_id))
        elif choice == '11':
            expense_id = int(input("Enter expense ID: "))
            print(Expense.get_expense_by_id(expense_id))
        elif choice == '12':
            user_id = int(input("Enter user ID: "))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            print(Expense.get_expenses_by_date_range(user_id, start_date, end_date))
        elif choice == '13':
            user_id = int(input("Enter user ID: "))
            print(Expense.get_total_amount_spent(user_id))
        elif choice == '14':
            name = input("Enter category name: ")
            description = input("Enter category description: ")
            Category.create_category(name, description)
        elif choice == '15':
            print(Category.get_all_categories())
        elif choice == '16':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
