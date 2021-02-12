where = input("Where should I look?")

if where == "in the bedroom":
    where_bedroom = input("Where in the bedroom should I look?")
    if where_bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

elif where == "in the bathroom":
    where_bathroom = input("Where in the bathroom should I look?")
    if where_bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")

elif where == "in the lab":
    where_lab = input("Where in the lab should I look?")
    if where_lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but I will keep looking.")