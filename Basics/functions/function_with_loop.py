def cross_bridge(steps):
    for distance in range(steps):
        print("Crossed step.")
    if distance > 5:
        print("the bridge is collapsing")
    else:
        print("We must keep going")

cross_bridge(3)
cross_bridge(6)