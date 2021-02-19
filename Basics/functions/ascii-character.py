print("Program Started")
asciiCode = abs(int(input("Please enter an ascii code:")))

if asciiCode in range(32,127):
    print(asciiCode)
    character = chr(asciiCode)
    print(f"The character represented by the ASCII code {asciiCode} is: {character}")
else:
    print("Invalid value")

print("Program ended!")