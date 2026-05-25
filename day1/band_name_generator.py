"""
Band Name Generator
-------------------
This program generates a Band Name based on the user's city and pet name.
 
Task: Ask user for their city name and pet name and
Combine them to generate a band name.
 
Test Case:
    Input : City = Hyderabad, Pet = Bruno
    Output: Your Band Name could be: Hyderabad Bruno
"""

print("Welcome to the Band Name Generator!")

user_city_name = input("Which city do you grow up in?\n")
user_pet_name = input("What is your Pet's name?\n")

ideal_band_name = user_city_name + " " + user_pet_name

# Below line will print the Band Name based on user's city and pet name
print("Your Band Name could be: " +ideal_band_name)