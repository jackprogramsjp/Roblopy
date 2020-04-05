from .utils.request import get

class Friends:
    @staticmethod
    def GetFriends(userId):
        return get("https://api.roblox.com/users/" + str(userId) + "/friends").json()

    @staticmethod
    def GetFirstFriend(userId):
        return get("https://api.roblox.com/users/" + str(userId) + "/friends").json()[-1]

    @staticmethod
    def GetRecentFriend(userId):
        return get("https://api.roblox.com/users/" + str(userId) + "/friends").json()[0]

    @staticmethod
    def UsersAreFriends(userId1, userId2):
        response1 = get("https://api.roblox.com/users/" + str(userId1) + "/friends").json()
        response2 = get("https://api.roblox.com/users/" + str(userId2) + "/friends").json()
        friends_list = [userId1, userId2]
        friendship = False

        for friends in response1:
            friends_list.append(friends["Id"])

        for friends in response2:
            friends_list.append(friends["Id"])

        for friend in friends_list:
            if friends_list.count(friend) > 1:
                friendship = True
                break

        return friendship
