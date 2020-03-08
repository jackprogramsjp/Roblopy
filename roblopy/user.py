import requests

class GetUserFromUsername:
    Id = None
    Username = None
    AvatarUri = None
    AvatarFinal = None
    IsOnline = None

    def __init__(self, username):
        response = requests.get("http://api.roblox.com/users/get-by-username?username=" + str(username)).json()

        try:
            response["Username"]
        except KeyError:
            print("GetUserFromUsername() Error: " + str(response["errorMessage"]))

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

        try:
            response["Username"]
        except KeyError:
            print("GetUserFromId() Error: " + str(response["errorMessage"]))

        self.Id = response["Id"]
        self.Username = response["Username"]
        self.AvatarUri = response["AvatarUri"]
        self.AvatarFinal = response["AvatarFinal"]
        self.IsOnline = response["IsOnline"]

class Users:
    @staticmethod
    def GetUsernameFromId(userId):
        response = requests.get("http://api.roblox.com/users/" + str(userId)).json()

        try:
            return response["Username"]
        except KeyError:
            return "User ID may not exist. Error: " + str(response["errors"])

    @staticmethod
    def GetIdFromUsername(username):
        response = requests.get("http://api.roblox.com/users/get-by-username?username=" + str(username)).json()

        try:
            return response["Id"]
        except KeyError:
            return response["errorMessage"]

    @staticmethod
    def CanManageAsset(userId, assetId):
        response = requests.get("http://api.roblox.com/users/" + str(userId) + "/canmanage/" + str(assetId)).json()

        try:
            return response["CanManage"]
        except KeyError:
            return response["errorMessage"]
