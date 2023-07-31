print("Welcome to your Love Calculator!")

name1 = input("Enter the first name:\n")
name2 = input("Enter the second name:\n")

name1 = name1.lower()
name2 = name2.lower()

combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true_value = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love_value = l + o + v + e

love_score = true_value + love_value


if love_score <10 or love_score > 85:
    print(f"Your love score is {love_score}! You go together like coke and mentos!")
elif 40 < love_score < 70:
    print(f"Your love score is {love_score}! Y'all are good!")
else:
    print(f"Your love score is {love_score}")

