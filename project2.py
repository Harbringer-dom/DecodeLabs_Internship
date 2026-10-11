def enter_expenses(expenses):
    print("Enter the expense details:")
    try:
        amount = float(input("Amount: "))
       
    except ValueError:
        
        print("Invalid amount. Please enter a numeric value.")
        return 0
    description = input("Description: ")
    category = input("Category: ")
    expenses.append({"amount": amount, "category": category, "description": description})
    print("Expense entered successfully!")
    return amount

# Display every saved expense, or a message when the list is empty.
def show_expenses(expenses):
    print("VIEW EXPENSES")
    if not expenses:
        print("No expenses to display.")
    else:
        print("Expenses: ")
        for expense in expenses:
            print(f"Amount: {expense['amount']} | Category: {expense['category']} | Description: {expense['description']}")

# Calculate overall spending and spending grouped by category.
def Calculations(expenses):      
    print("CALCULATE TOTALS")
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {round(total,2)}")

    # Add each expense amount to its matching category total.
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']

        else:
            category_totals[category] = expense['amount']

    print("Expenses by Category: ")

    # Sort categories from the highest total to the lowest total.
    items = list(category_totals.items())
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

                

    for category, total in items:
        print(f"Category: {category} | Total: {round(total,2)}")

    if category_totals:
        Highest_category = max(category_totals , key=category_totals.get)
        print(f"Highest Expense Category: {Highest_category}")
    return total, category_totals

def main():
    # Keep expenses available while the program is running.
    expenses = []
    total_expenses = 0
    while True:
        # Show the menu repeatedly until the user chooses to exit.
        print("\nExpense Tracker Menu")
        print("1. Enter Expense")
        print("2. View Expenses")
        print("3. Calculate Totals")
        print("4. Exit")
        choice = input("Choose a menu option (1-4): ").strip()

        if choice == "1":
            # Option 1 adds a new expense.
            print()
            amount = enter_expenses(expenses)
            total_expenses += amount
            print(f"Total_Expense: {round(total_expenses,2)}")
        elif choice == "2":
            # Option 2 displays all saved expenses.
            print()
            show_expenses(expenses)
        elif choice == "3":
            # Option 3 calculates totals for all saved expenses.
            print()
            Calculations(expenses)
        elif choice == "4":
            # Option 4 ends the program.
            print(f"\n Exiting. Final:{round(total_expenses,2)}")
            break
        else:
            print("Invalid option. Please choose again.") 

if __name__ == "__main__":
    main()