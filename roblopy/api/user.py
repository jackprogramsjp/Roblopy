import urllib.request
import json

class _User:
    Id = None
    Username = None
    AvatarUri = None
    AvatarFinal = None
    IsOnline = None

    def __init__(self, data):
        self.Id = data["Id"]
        self.Username = data["Username"]
        self.AvatarUri = data["AvatarUri"]
        self.AvatarFinal = data["AvatarFinal"]
        self.IsOnline = data["IsOnline"]

class Users:
    @staticmethod
    def GetUsernameById(id):
        response = urllib.request.urlopen("http://api.roblox.com/users/" + str(id))
        return json.loads(response.read())["Username"]

    @staticmethod
    def GetIdByUsername(username):
        response = urllib.request.urlopen("http://api.roblox.com/users/get-by-username?username=" + str(username))
        return json.loads(response.read())["Id"]

    @staticmethod
    def User(username):
        response = urllib.request.urlopen("https://api.roblox.com/users/get-by-username?username=" + str(username))
        return _User(json.loads(response.read()))

    @staticmethod
    def UserById(id):
        response = urllib.request.urlopen("https://api.roblox.com/users/" + str(id))
        return _User(json.loads(response.read()))

    @staticmethod
    def UserCanManageAsset(id, assetId):
        response = urllib.request.urlopen("http://api.roblox.com/users/" + str(id) + "/canmanage/" + str(assetId))
        return json.loads(response.read())["CanManage"]
