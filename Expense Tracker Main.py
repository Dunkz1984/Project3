#The code should build an expense tracker that allows users to:
# Add an expense
# Update an expense
# Delete an expense
# View all expenses
# View a summary of expenses
# View a summary of expenses for a specific month (of the current year)
#
# Additionally, users could:
# Add expense categories and allow users to fulter expenses by category.
# Allow users to set a budget for each month and show a warning when the user exceeds the budget.
# Allow users to export expenses to a CSV file.

# The roadmap website suggests using argparse. I don't know what this is, so I will look it up.

import argparse
import json
# The way too useful but ultimately quite annoying AI features in VSCode have suggested import csv. I have worked with JSON files; csv shouldn't be too different.

filepath = "Type 3.json"


def add_expense(description, amount):
    with open(filepath, 'r') as file:
        expenses = json.load(file)
        if not expenses:
            new_id = 1
        else:
            new_id = expenses[-1]["id"] + 1
    
    new_expense = {"id": new_id, "description": description, "amount": amount}
    expenses.append(new_expense)

def delete_expenses(id):
    with open(filepath, 'r') as file:
        expenses = json.load(file)
    updated_expenses = [expenses for y in expenses if y["id"] != id]
    if len(expenses) == len(updated_expenses):
        print(f"Cannot delete. ID does not exist.")
    else:
        with open(filepath, 'w') as file:
            json.dump(updated_expenses, file)
            print(f"Successfully deleted expense with ID {id}.")

def list_expenses():
    
    


def main():
    parser = argparse.ArgumentParser(description="An Expense Tracker")
    parser.add_argument("--description", "-d", help="Description of the expense")
    parser.add_argument("--amount", "-a", help="Amount of the expense", type=float)
    parser.add_argument("--id", "-i", help="ID of the expense", type=int)
    parser.add_argument("--month", "-m", help="Month of the expense")
    
    args = parser.parse_args()

    command = input("Enter a command: ")

    #What I need here are simple commands: add, delete, list, summary.
    if command.startswith("add"):
        add_expense(args.description, args.amount)
    elif command.startswith("delete"):
        delete_expenses(args.id)
    elif command.startswith("list"):
        print("List of expenses")
        list_expenses()




if __name__ == "__main__":
    main()

