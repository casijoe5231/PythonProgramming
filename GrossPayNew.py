hours = input("Enter Hours:")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a numeric value for Hour!")
    quit()


rate =input("Enter Rate:")
try:
    rate = float(rate)
except ValueError:
    print("Please enter a numeric value for Rate!")
    quit()

if hours > 40:
    overtime = hours - 40
    gross_pay = round((hours*rate)+(1.5*overtime*rate),2)
else:
    gross_pay = round(hours * rate,2)

print("Gross Pay: ", gross_pay)

