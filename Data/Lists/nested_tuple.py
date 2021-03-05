def steps():
    likelihoods = [
        ("step1", 50),
        ("step2", 38),
        ("step3", 27),
        ("step4", 99),
        ("step5", 4),
        ]

    return likelihoods

def run():
    data = steps()
    good_steps = []
    bad_steps = []

    for item in data:
        if item[1] >= 50:
            bad_steps.append(item)
        else:
            good_steps.append(item)
    print(f"Good steps: {len(good_steps)} Bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run()
