def likelihood():
    likelihoods = (50,38,20)
    return likelihoods


def run():
    likelihoods = likelihood()
    print(f"Min likliehood of falling: {min(likelihoods)}")

if __name__ == "__main__":
    run()