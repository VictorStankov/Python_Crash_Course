import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


filename = 'username.json'
with open(filename) as f_obj:
    username_0 = json.load(f_obj)
    response = input(f"Is '{username_0}' your username? ")
    if response.lower() == 'yes':
        greet_user()
    elif response.lower() == 'no':
        get_new_username()
