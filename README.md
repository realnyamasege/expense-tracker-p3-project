"""

# Expense Tracker

An Expense Tracker application to manage personal expenses and user accounts. This project includes functionalities to create, read, update, and delete both users and expenses, as well as additional features for viewing expenses by date range and calculating total amounts spent.

## Project Structure

The following structure is implemented within this single file:

- Database functions
- User class
- Expense class
- Category class
- Main application

## Setup Instructions

### Prerequisites

- Python 3.x
- SQLite

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/realnyamasege/expense-tracker-p3-project

   ```

2. **Install dependencies** (if any required libraries are missing):

   ```bash
   pip install sqlite3
   ```

3. **Initialize the database**:
   ```bash
   python -c 'from expense_tracker import init_db; init_db()'
   ```

## Usage

Run the main application:

```bash
python main.py
```
