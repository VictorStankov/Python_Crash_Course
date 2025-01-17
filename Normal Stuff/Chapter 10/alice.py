filename = 'text_files/alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, but the file {filename} does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} has about {str(num_words)} words.')