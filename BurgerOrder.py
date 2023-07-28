print("Welcome to the Chop Top Burgirs!")
print("Please enter your order based on the questions below:")
size = input("Please enter the burger size you prefer:\n")
#Burger size logic
# def get_burger_size(size):
#     while True:
#             if size() not in ('M', 'N', 'L'):
#                 print("Please enter M for Mini, N for Normal, or L for Large\n")
#             else:
#                 break
#     return size

add_mushroom = input("Please let us know whether you want mushrooms in the burger\n")
# """ #Mushroom logic
# """ def get_mushroom_value(add_mushroom):
#     while True:
#             if add_mushroom() not in ('Yes', 'No'):
#                 print("Please enter Yes or No!\n")
#             else:
#                 break
#     return add_mushroom """ """

cheese = input("Do you want extra cheese in the burger?\n")
# """ #Cheesy logic
# """ def get_cheese_value(cheese):
#     while True:
#             if cheese() not in ('Yes', 'No'):
#                 print("Please enter Yes or No!\n")
#             else:
#                 break
#     return cheese """ """

burger_price = 0
if size == "M":
    burger_price += 5
elif size == "N":
    burger_price += 8
elif size == "L":
    burger_price += 10  

mush_price = 0
if add_mushroom == "Yes":
    mush_price += 1
elif add_mushroom == "No":
    mush_price += 0

cheese_price = 0
if cheese == "Yes":
    cheese_price += 1
elif cheese == "No":
    cheese_price += 0


#Total value
print(f"Your total order value is {burger_price+mush_price+cheese_price}")