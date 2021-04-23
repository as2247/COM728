import matplotlib.pyplot as plt


def small():
    x = [4, 4, 6, 6, 4]
    y = [4, 6, 6, 4, 4]
    plt.plot(x, y, "ro:")


def medium():
    x = [3, 3, 7, 7, 3]
    y = [3, 7, 7, 3, 3]
    plt.plot(x, y, "gs--")


def large():
    x = [2, 2, 8, 8, 2]
    y = [2, 8, 8, 2, 2]
    plt.plot(x, y, "bp-")


def run():
    print("Running...")
    small()
    medium()
    large()
    plt.show()


run()