import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}

    line_type = input("What type of line would you like (:, -- or -)?")
    line_colour = input("What colour line would you like? (r, g or b)")
    marker_style = input("What style marker would you like? (o, s or ^)")

    paths['line_type'] = line_type
    paths['line_colour'] = line_colour
    paths['marker_style'] = marker_style

    return paths


def generate():
    line_num = int(input("How many lines would you like to display?"))

    for line_num in range(line_num):
        values = data()
        x = rnd.sample(range(1,10), 5)
        y = rnd.sample(range(1,10), 5)

        formatting = f"{values['line_type']}{values['line_colour']}{values['marker_style']}"
        plt.plot(x, y, formatting)
        plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


run()