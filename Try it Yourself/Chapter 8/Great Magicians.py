def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician.title())


def make_great(magicians_list):
    # return [magician.title() + ' the Great' for magician in magicians_list]
    # for magician in magicians_list:
    #     magician_edited = magician.title() + ' the Great'
    #     edited_magicians.append(magician_edited)
    # return edited_magicians
    edited_magicians = []
    for magician in magicians_list:
        edited_magician = magician.title() + ' the Great'
        edited_magicians.append(edited_magician)
    magicians[:] = edited_magicians[:]
    return magicians


magicians = ['astor', 'houdini', 'penn', 'teller']
print(make_great(magicians))
print(show_magicians(magicians))
