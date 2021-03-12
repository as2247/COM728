def observed():
    observations = []
    for count in range(5):
        obs = input("Please Enter an Observation:")
        observations.append(obs)
    return observations


def remove_observations(observations):
    is_running = True
    while is_running:
        response = input("Do you wish to remove an observation? (yes/no)")
        if response == "yes":
            delete = input("Please enter the observation you wish to delete")
            observations.remove(delete)
        else:
            is_running = False


def run():
    print("Counting Observations...")
    observations = observed()
    remove_observations(observations)

    # Create a set here
    create_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        create_set.add(data)

    # Display the set here
    for data in sorted(create_set):
        print(f"{data[0]} observed {data[1]} times")


if __name__ == "__main__":
    run()