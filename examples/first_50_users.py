from roblopy import User, BadRequest

for i in range(1, 51):
    try:
        user = User(i)
    except BadRequest:
        pass
    else:
        print("==========")
        print("Username: " + user.Username)
        print("UserId: " + str(user.Id))