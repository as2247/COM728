number = int(input("Please enter a number"))

factorial = 1
count = 0

while count < number:
    count += 1
    factorial = factorial * count

print(f"Factorial is:  {factorial}")