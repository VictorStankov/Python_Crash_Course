filename = 'text_files/responses.txt'

while True:
    with open(filename, 'a') as file_object:
        response = input("Please enter the reason you like programming: ")
        if response == 'q':
            break
        else:
            file_object.write(f"{response}\n")
