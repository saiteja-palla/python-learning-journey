"""
Rollercoaster Ticket Pricing
-----------------------------
This project determines whether the user is eligible to ride or not
based on their height, and calculates the final ticket price including
an optional photo package.

Ticket Pricing:
    - Height < 120cm  : Not eligible for ride
    - Age < 12        : $5 (Child)
    - Age 12 to 18    : $7 (Youth)
    - Age 19 to 44    : $12 (Adult)
    - Age >= 45       : Free ride
    - Photo package   : +$3 (optional)

Test Case:
    Input : Height = 150cm, Age = 25, Photo = 1
    Output: The final ticket price is $15
"""

ticket_price = 0
user_height = float(input("Whats your height in cm? "))

if user_height < 120:
    print("Sorry, your height is not eligible for a ride.")

else:
    age = int(input("Whats your age? "))

    if age < 12:
        ticket_price = 5
        print("Child tickets are $5")
    elif 12 <= age <= 18:
        ticket_price = 7
        print("Youth tickets are $7")
    elif 18 < age < 45:
        ticket_price = 12
        print("Adult tickets are $12")
    else:
        print("We offer you a free ride :) ")

    want_a_photo = input("Do you want a photo (chargable)? press 1 if yes and 0 if no: ")

    if want_a_photo == "1":
        ticket_price += 3
    
    if ticket_price == 0:
          print(f"Enjoy your free ride! No charges :)")
    else:
        print(f"The final ticket price is ${ticket_price}")
    