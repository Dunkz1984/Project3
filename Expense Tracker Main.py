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

def add_expense(expense):
    with open(filepath, "r") as file:
        data= json.load(file)
        data.append(expense)


def update_expense(expense):

def delete_expense(expense):

def view_expenses():

def view_summary():

def view_month_summary(month):





def main():
    parser = argparse.ArgumentParser(description="An Expense Tracker")
    parser.add_argument("-a", "--add", help="Add an expense")
    parser.add_argument("-u", "--update", help="Update an expense")
    parser.add_argument("-d", "--delete", help="Delete an expense")
    parser.add_argument("-v", "--view", help="View all expenses")
    parser.add_argument("-s", "--summary", help="View a summary of expenses")
    parser.add_argument("-m", "--month", help="Type the number of the month to get a summary for that month", type=int)
    
    args = parser.parse_args()
    
    if args.add:
        add_expense(args.add)
    elif args.update:
        update_expense(args.update)
    elif args.delete:
        delete_expense(args.delete)
    elif args.view:
        view_expenses()
    elif args.summary:
        view_summary()
    elif args.month:
        view_month_summary(args.month)
    else:
        print("No arguments provided. Please provide an argument.")

if __name__ == "__main__":
    main()

