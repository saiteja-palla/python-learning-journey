"""
Tip Calculator
--------------
This program finds the split that each person has to pay including the tip amount.

Task: Ask user for the total bill, tip percentage and no.of person sharing bill.
Calculate the share of each person including the tip amount (rounded to 2 decimal points).

Test Case: 
    input : Bill = 150, Tip = 12, People = 3
    output : Each person pays = $56.0
"""

print("Welcome to Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage of tip would you like to add <10 12 15 20>? "))
no_of_persons = int(input("How many people to split the bill?"))

tip_on_bill = bill * tip_percentage / 100

total_bill = bill + tip_on_bill

bill_per_person = total_bill/no_of_persons

#Below line will print the share of each person has to pay based on user's total bill, tip included and number of persons to share the bill
print(f"Each person should pay: ${round(bill_per_person,2)}")
