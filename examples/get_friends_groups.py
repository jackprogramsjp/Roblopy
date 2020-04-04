from roblopy import Users, Friends, Groups

MyUserId = Users.GetIdFromUsername("NoobsterStudio")

for user in Friends.GetFriends(MyUserId):
    userId = user["Id"]
    group = Groups.GetUsersGroups(userId)

    print(group)