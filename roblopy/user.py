from .utils.request import get

class User:
    Id = None
    Username = None

    def __init__(self, userId):
        response = get("http://api.roblox.com/users/" + str(userId)).json()

        self.Id = response["Id"]
        self.Username = response["Username"]

class Users:
    @staticmethod
    def GetUsernameFromId(userId):
        return get("http://api.roblox.com/users/" + str(userId)).json()["Username"]

    @staticmethod
    def GetIdFromUsername(username):
        return get("http://api.roblox.com/users/get-by-username?username=" + str(username)).json()["Id"]

    @staticmethod
    def IsOnline(userId):
        return get(f"https://api.roblox.com/users/{userId}/onlinestatus/").json()["IsOnline"]

    @staticmethod
    def GetOnlineStatus(userId):
        return get(f"https://api.roblox.com/users/{userId}/onlinestatus/").json()

    @staticmethod
    def CanManageAsset(userId, assetId):
        return get("http://api.roblox.com/users/" + str(userId) + "/canmanage/" + str(assetId)).json() \
            ["CanManage"]
