import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n--- All Expenses ---")

        found = False

        for expense in reader:
            found = True
            print(
                f"Date: {expense['Date']} | "
                f"Category: {expense['Category']} | "
                f"Description: {expense['Description']} | "
                f"Amount: Rs. {expense['Amount']}"
            )

        if not found:
            print("No expenses found.")


def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            total += float(expense["Amount"])

    print(f"\nTotal Expenses: Rs. {total:.2f}")


def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n--- Category Summary ---")

    for category, amount in categories.items():
        print(f"{category}: Rs. {amount:.2f}")


def main():
    while True:
        print("\n==============================")
        print("      PYTHON EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
