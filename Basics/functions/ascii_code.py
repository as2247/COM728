print("Program Started")
letter = input("Please enter a standard character:")

if len(letter) == 1:
    print(letter)
    ascii = ord(letter)
    print(f"The ASCII code for {letter} is: {ascii}")
    print("Program Ended")
else:
    print("Please enter a single valid character ")


