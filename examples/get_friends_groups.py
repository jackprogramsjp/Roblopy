from roblopy import Users, Friends, Groups

MyUserId = Users.GetIdFromUsername("Coeptus")

for user in Friends.GetFriends(MyUserId):
    userId = user["Id"]
    group = Groups.GetUsersGroups(userId)

    print(group)
