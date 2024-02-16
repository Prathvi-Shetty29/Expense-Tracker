import calendar
import datetime
from expense import Expense


def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path="expenses.csv"
    budget =2000
    # Get user expense
    expense = get_user_expense()
    

    # Write it to file
    save_expense_toFile(expense,expense_file_path)

    # Read file and summerize expense
    summerize_expense(expense_file_path,budget)

    

def get_user_expense():
    print(f"🎯 Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    
    expense_category = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Miscellaneous",
    ]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f"    {i+1}.{category_name}")

        value_range =f"1 - {len(expense_category)}"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        except Exception:
            print("Invalid !!!!!")
    
        if selected_index in range(0,len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. please try again")


def save_expense_toFile(expense: Expense, expense_file_path: str):
    print(f"🎯 Saving user Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summerize_expense(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense!")
    expenses:list[Expense] = []
    with  open(expense_file_path,"r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name,expense_amount,expense_category = stripped_line.split(",")
            
            line_expense = Expense(name = expense_name,category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)
    amount_by_category={}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] +=expense.amount
        else:
             amount_by_category[key] =expense.amount
    
    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ₹{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ₹{total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ₹{remaining_budget:.2f}")
    
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    if(daily_budget<=50):
        print(red(f"👉 Budget Per Day: ₹{daily_budget:.2f}"))
    else:
        print(green(f"👉 Budget Per Day: ₹{daily_budget:.2f}"))

    


def green(text):
    return f"\033[92m{text}\033[0m"

def red(text):
    return f"\033[91m{text}\033[0m"


if __name__ == "__main__":
    main()

