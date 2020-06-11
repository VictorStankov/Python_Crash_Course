filename = 'text_files/guest_book.txt'

while True:
    with open(filename, 'a') as file_object:
        name = input("Please enter your name: ")
        if name == 'q':
            break
        else:
            file_object.write(f"{name.title()} visited the program.\n")
