print("=== Expense Tracker ===")

expenses = []
amounts = []

n = int(input("Enter number of expenses: "))

for i in range(n):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    expenses.append(name)
    amounts.append(amount)

print("\n--- Expenses List ---")

for i in range(n):
    print(expenses[i], "-", amounts[i])

# Total Expense
total = 0
for amt in amounts:
    total = total + amt

print("\nTotal Expense:", total)

# Highest Expense
max_amount = amounts[0]
max_index = 0

for i in range(1, n):
    if amounts[i] > max_amount:
        max_amount = amounts[i]
        max_index = i

print("Highest Expense:", expenses[max_index])