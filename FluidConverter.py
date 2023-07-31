def fluid_ounces(x):
    mililiters = 29.57353 * x
    print(f"The same in ml is {mililiters} ml")


x = int(input("The fluid ounces that you have is: "))
fluid_ounces(x)