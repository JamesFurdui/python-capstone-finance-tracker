# Capstone Project - Finance Tracker

print("Welcome to the Personal Finance Tracker!")

admin_input = ""
expense_category = {}

def view_expenses(expense_category):
    for key, value in expense_category.items():
        print(f"Category: {key}")
        for expense in value:
            print(f"    - {expense[0]}: ${expense[1]:.2f}")

def view_summary(expense_category):
    print("Summary: ")
    total_value = 0
    for key, value in expense_category.items():
        print(f"{key}:", end=" ")
        for expense in value:
            category_total = expense[1]
            total_value += category_total
        print(f"${total_value:.2f}") 



while True:
    try:
        user_input = int(input("What would you like to do?\n1. Add Expense\n2. View All Expenses\n3. View Summary\n4. Exit\nChoose an option (1-4): "))
    
        if user_input > 4 or user_input < 1:
            raise ValueError()

        if user_input == 1:
            try:
                description = input("Enter expense description: ")
                if not category.isalpha():
                    raise ValueError("Description must contain letters.")
                category = input("Enter category: ")
                if not category.isalpha():
                    raise ValueError("Category must contain letters.")
                amount = float(input("Enter amount: "))
                if amount < 0:
                    raise ValueError("Amount must be a positive number.")    
            except ValueError as ve:
                print(f"Invalid input error: {ve}")
            else:
                expense_info = tuple((description, amount))
                # If the specified category exists, append a new tuple to said category, if it doesn't
                # create a new category and add the expense_info to it
                if category in expense_category: 
                    expense_category[category].append(expense_info)
                else: 
                    expense_category[category] = [expense_info]
                print("Expense added successfully.")
        if user_input == 2:
            view_expenses(expense_category)
        if user_input == 3:
            view_summary(expense_category)
        if user_input == 4:
            print("Thank you for using the Finance Tracker!!")
            break
    except ValueError:
        print("Only numbers 1-4 are allowed.")
