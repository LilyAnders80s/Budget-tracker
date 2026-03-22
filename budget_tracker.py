# Budget Tracker Program

# Store income
income = 0

# List to store expenses
expenses = []

# Ask user for income
income = int(input("Enter your income: "))

# Loop to add expenses
while True:
    name = input("Enter expense name (or 'done' to finish): ")
    
    # Stop loop if user is finished
    if name.lower() == "done":
        break
    
    # Get expense amount
    amount = int(input("Enter expense amount: "))
    
    # Add to expenses list
    expenses.append(amount)

# Calculate total expenses
total_expenses = sum(expenses)

# Calculate remaining balance
balance = income - total_expenses

# Display results
print("Total Income:", income)
print("Total Expenses:", total_expenses)
print("Remaining Balance:", balance)

# Check for overspending
if balance < 0:
    print("Warning: You are over budget!")
