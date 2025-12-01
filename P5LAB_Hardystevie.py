# Stevie Hardy
# Date: 12/01/2025
# Assignment: P5LAB - Self Checkout Simulation
# Description: Simulates a self-checkout machine, calculates change in coins and bills.

import random

def disperse_change(change):
    """Breaks down change into dollars, quarters, dimes, nickels, and pennies."""
    # Convert to cents to avoid floating-point issues
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    # Display results
    print("Change breakdown:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    # Generate random owed amount
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${owed}")

    # Prompt user for cash input
    cash = float(input("Enter the amount of cash you will put into the machine: $"))

    # Calculate change
    if cash < owed:
        print("Insufficient funds. Transaction canceled.")
    else:
        change = cash - owed
        print(f"Change owed: ${change:.2f}")
        disperse_change(change)

# Call main function
main()