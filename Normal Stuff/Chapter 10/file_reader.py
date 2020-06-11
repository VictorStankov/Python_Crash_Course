with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

print()

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print()

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())
