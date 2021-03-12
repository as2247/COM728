def observed():
    observations = []

    for count in range(7):
        obs = input("Please enter an observation")
        observations.append(obs)
    return observations


def run():
    print("Counting Observations")
    observations = observed()

    create_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        create_set.add(data)

    for data in create_set:
        print(f"{data[0]} observed {data[1]} times")


if __name__ == "__main__":
    run()
