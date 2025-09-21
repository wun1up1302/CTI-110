# Stevie Hardy
# 09/21/2025
# P1HW2 – Travel Budget Calculator
# This program asks the user for their travel budget and expenses, then calculates and displays the remaining balance.

# Pseudocode:
# 1. Prompt user to enter budget
# 2. Prompt user to enter travel destination
# 3. Prompt user to enter gas cost
# 4. Prompt user to enter accommodation cost
# 5. Prompt user to enter food cost
# 6. Add all expenses
# 7. Subtract expenses from budget
# 8. Display travel summary and remaining balance

print("This program calculates and displays travel expenses.\n")

# Collect user input
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n----------Travel Expenses----------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print("-----------------------------------")
print(f"Remaining Balance: ${remaining_balance:.2f}")
