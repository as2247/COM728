cover_type = input("What type of cover does the book have (hard or soft)?")
print(cover_type)

if cover_type == 'soft':
    perfect_bound = input("Is the book perfect-bound?")

    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    elif perfect_bound == "not sure":
        print("hmmm... a mystery")
    else:
        print("Soft covers with coils or stitches are great for short books")

elif cover_type == 'hard':
    print("Books with hard covers can be more expensive!")

else:
    print("That is not a valid answer")
