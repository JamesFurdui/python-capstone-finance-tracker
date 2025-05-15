# python-capstone-finance-tracker

This is the Finance Tracker project that I have worked on. It allows the user to
add an expense, view all their expenses, view a summary of their expenses, or exit the program. Once run, the program asks the user what option they would like to choose from 4 different options. Typing in an invalid option will provide the user with an error and re-prompt the user to choose an option between 1-4. 

Choosing option 1 (Add Expense) will prompt the user for a description of the expense, what category the expense is (food, work, etc.), and then the amount of the expense. If any of the values are not what the program wants such as a number for the category, or a word for the amount, then an error will be provided and the user will return to the main menu screen.

Choosing option 2 (View All Expenses) will display all the expenses that the user has added during runtime. One thing to note is that if the user adds another expense with the same category, the expense will be added to that category (For example, if there is 'food' category that has an apple in it, then adding another fruit like a banana with the category of 'food' will put both fruits under the same category and will not make a new category).

Choosing option 3 (View Summary) shows a summary of all the expenses of each category.

Choosing option 4 (Exit) will close down the program.

HOW TO RUN: There is not too much that goes into running the script for this project. There are no other files (such as a file that saves data between runtimes), so the only thing is to run the program and choose any of the options provided in the program.

CONCEPTS USED:
- Functions
- Loops
- Dictionaries
- Tuples
- Conditional statements (if, else)
- Exception Handling (try, except, raising flags)
- User input and output