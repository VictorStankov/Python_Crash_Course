def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = f"Sorry, but the file {filename} does not exist."
        # print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has about {str(num_words)} words.')


filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick', 'text_files/little_women.txt']
for filename in filenames:
    count_words(filename)
