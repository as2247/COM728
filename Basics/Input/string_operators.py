lives = int(input("Please enter your number of lives"))
print(lives)

energy_level = int(input("Please enter your energy level"))
print(energy_level)

shield_level = int(input("Please enter your sheild level"))
print(shield_level)

print("Health has been set")
print(f"Lives:  " + (lives * '♥'))
print(f"Energy: " + (energy_level * '♦'))
print(f"Shield: " + (shield_level * '♦'))
