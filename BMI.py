print("Check your BMI in this app!")

height = input("What is your height in m? (1 feet is 0.3 m)\n")

weight = input("What is your weight? in kg\n")

height = float(height)
weight = float(weight)

bmi = round(weight/(height*height),2)

print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight!")
elif 18.5<bmi<25:
    print("You are normal!")
elif 25<bmi<30:
    print("You are overweight!")
elif 30<bmi<35:
    print("You are obese!")
else:
    print("Please enter the correct value!")
