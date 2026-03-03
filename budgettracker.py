income = float(input("Enter your income: "))
print()

expense_dictionary = {}

while True:
    expense = input("Enter your expense category (Press enter to exit): ")
    if expense == "":
        break
    amount = float(input(f"Enter your expense amount for {expense}: "))
    print()
    expense_dictionary[expense] = amount

print()
print("Your Budget Summary")
print("--------------------")
print(f"Income: {income}")
print(f"Expenses: {sum(expense_dictionary.values())}")
print("--------------------")
print("Your Expenses")
for k, v in expense_dictionary.items():
    print(f"Expense for {k}: {v}")