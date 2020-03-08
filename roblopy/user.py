import requests

class GetUserFromUsername:
    Id = None
    Username = None
    AvatarUri = None
    AvatarFinal = None
    IsOnline = None

    def __init__(self, username):
        response = requests.get("http://api.roblox.com/users/get-by-username?username=" + str(username)).json()

        self.Id = response["Id"]
        self.Username = response["Username"]
        self.AvatarUri = response["AvatarUri"]
        self.AvatarFinal = response["AvatarFinal"]
        self.IsOnline = response["IsOnline"]

class GetUserFromId:
    Id = None
    Username = None
    AvatarUri = None
    AvatarFinal = None
    IsOnline = None

    def __init__(self, userId):
        response = requests.get("http://api.roblox.com/users/" + str(userId)).json()

        self.Id = response["Id"]
        self.Username = response["Username"]
        self.AvatarUri = response["AvatarUri"]
        self.AvatarFinal = response["AvatarFinal"]
        self.IsOnline = response["IsOnline"]

class Users:
    @staticmethod
    def GetUsernameFromId(userId):
        return requests.get("http://api.roblox.com/users/" + str(userId)).json()["Username"]

    @staticmethod
    def GetIdFromUsername(username):
        return requests.get("http://api.roblox.com/users/get-by-username?username=" + str(username)).json()["Id"]

    @staticmethod
    def CanManageAsset(userId, assetId):
        return requests.get("http://api.roblox.com/users/" + str(userId) + "/canmanage/" + str(assetId)).json() \
            ["CanManage"]
