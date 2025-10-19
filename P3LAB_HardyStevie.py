# P3LAB_HardyStevie
# This program calculates the most efficient number of dollars, quarters,
# dimes, nickels, and pennies needed to make a given amount of money.
# Stevie Hardy
# Date: October 19, 2025
# Course: CTI-110-0003 

# Get user input
amount = float(input("Enter a money amount (e.g., 4.37): "))

# Convert to cents for easier calculation
cents = int(round(amount * 100))

# Calculate coin counts
dollars = cents // 100
cents -= dollars * 100

quarters = cents // 25
cents -= quarters * 25 

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

# Display results with correct singular/plural formatting
if dollars == 1:
    print("1 dollar")
elif dollars > 1:
    print(f"{dollars} dollars")

if quarters == 1:
    print("1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

if dimes == 1:
    print("1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

if nickels == 1:
    print("1 nickel")
elif nickels > 1:
    print(f"{nickels} nickels")

if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")

