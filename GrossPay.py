hours = input("Enter Hours:")

rate =input("Enter Rate:")
hours = float(hours)
rate = float(rate)

if hours > 40:
    overtime = hours - 40
    gross_pay = round((hours*rate)+(1.5*overtime*rate),2)
else:
    gross_pay = round(hours * rate,2)

print("Gross Pay: ", gross_pay)

