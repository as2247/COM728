num1 = int(input("Please enter the first whole number."))
num2 = int(input("Please enter the second whole number."))
num3 = int(input("Please enter the third whole number."))

even = 0
odd = 0

if num1 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if num2 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if num3 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

print(f"There were {even} even numbers and {odd} odd numbers")