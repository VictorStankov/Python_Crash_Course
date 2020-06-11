filename = 'text_files/cats.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents.strip())
except FileNotFoundError:
    pass

print()

filename = 'text_files/dogs.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents.strip())
except FileNotFoundError:
    pass
