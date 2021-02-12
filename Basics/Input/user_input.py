name = input("What is your name?")
print(f"It's nice to meet you {name}")

age = int(input("How old are you (years)?"))
print(age)

height = float(input("How tall are you (m)"))
print(height)

weight = float(input("How much do you weigh (Kg)"))
print(weight)

bmi = (weight/(height**2))

print(f"{name} you are {age} years old and your bmi is {bmi}")

