current_users=['paul','eric','john','frank','carlos']
new_users=['jessica','pablo','Paul','tim','fRank']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, that username has already been used!")
    else:print("That username is available.")