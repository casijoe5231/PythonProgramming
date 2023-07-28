print("Welcome to the Trip Cost Calculator!")

days = input("How long are you planning to stay?\n")
room = input("Which room would you prefer?\n Please enter your respons between Standard, Deluxe, and Premium\n")
additional = input("Do you require any additional amenities?\n Please enter Yes or No\n")
food = input("Do you want Breakfast, Lunch or Dinner? If yes, please answer with the meal\n")


days = float(days)
room_price = 0
additional_price = 0
food_price = 0


if room == "Standard":
    room_price = 50
elif room == "Deluxe":
    room_price = 75
elif room == "Premium":
    room_price = 100
else:
    print("Please enter the correct room name!")

if additional == "Yes":
    additional_price = 20
elif additional == "No":
    additional_price = 0
else:
    print("Please enter the right response!")

if food == "Breakfast":
    food_price = 10
elif food == "Lunch":
    food_price = 20
elif food == "Dinner":
    food_price = 30
elif food == "No":
    food_price = 0
else:
    print("Please enter the correct response!")

total_cost = days * (room_price+additional_price+food_price)

print(f"The total cost of your room is {total_cost} dollars.")



