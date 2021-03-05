def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction")
    dirs = directions()
    for index in range(len(dirs)):
        direction = dirs[index]
        print(f"{index}: {direction}")

    selected_option = int(input())
    return dirs[selected_option]

def run():
    route = []

    for _ in range(5):
        direction = menu()
        route.append(direction)
    print(f"Escape Route: {route}")


if __name__ == "__main__":
    run()