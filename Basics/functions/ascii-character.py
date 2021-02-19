print("Program Started")
asciiCode = abs(int(input("Please enter an ascii code:")))

if asciiCode in range(32,126,1):
    print(asciiCode)
    character = chr(asciiCode)
    print(f"The character represented by the ASCII code {asciiCode} is: {character}")

print("Program ended!")