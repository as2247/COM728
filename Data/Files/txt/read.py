def display_chars(file_path, no_chars):
    print("The first 5 characters are:")
    with open(file_path) as file:
        no_chars_read = file.read(no_chars)
    print(no_chars_read)
    print("")

def display_line(file_path):
    print("The first line is:")
    with open(file_path) as file:
        line = file.readline().strip()
    print(line)
    print("")

def display_text(file_path):
    print("The full text is:")
    with open(file_path) as file:
        data = file.read()
        file.close()
    print(data)
    print("")

def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()
