filename = 'text_files/communist_manifesto.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
    words = contents.lower().split()
    print(words.count('communism'))
    print(words.count('the'))
