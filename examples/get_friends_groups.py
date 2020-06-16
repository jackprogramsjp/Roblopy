from roblopy import Users, Friends, Groups

my_user_Id = Users.get_id_from_username("Coeptus")

for user in Friends.get_friends(my_user_Id):
    user_id = user["Id"]
    group = Groups.get_users_groups(user_id)

    print(group)
