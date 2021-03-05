def display_chars(file_path, no_chars):
    with open("./library.txt") as file:
        no_chars_read = file.read(no_chars)
    print(no_chars_read)

def display_line(file_path):
    with open("./library.txt") as file:
        line = file.readline().strip()

def run()

if __name__ == "__main__":
    run()
