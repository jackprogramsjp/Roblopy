from bs4 import BeautifulSoup
from .utils.request import get, no_data_get

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
    def IsInGroup(userId, groupId):
        response = get(f"https://api.roblox.com/users/{userId}/groups").json()
        in_group = False

        for group in response:
            if group["Id"] == groupId:
                in_group = True
                break

        return in_group

    @staticmethod
    def GetRankInGroup(userId, groupId):
        response = get(f"https://api.roblox.com/users/{userId}/groups").json()
        rank = None

        for group in response:
            if group["Id"] == groupId:
                rank = group["Rank"]
                break

        return rank

    @staticmethod
    def GetRoleInGroup(userId, groupId):
        response = get(f"https://api.roblox.com/users/{userId}/groups").json()
        role = None

        for group in response:
            if group["Id"] == groupId:
                role = group["Role"]
                break

        return role

    @staticmethod
    def GroupIsPrimary(userId, groupId):
        response = get(f"https://api.roblox.com/users/{userId}/groups").json()
        primary = False

        for group in response:
            if group["Id"] == groupId and group["IsPrimary"]:
                primary = True
                break

        return primary

    @staticmethod
    def GetProfileDescription(userId):
        response = no_data_get(f"https://www.roblox.com/users/{userId}/profile").content
        soup = BeautifulSoup(response, "html.parser")

        try:
            description = soup.find("span", {"class": "profile-about-content-text linkify"}, text=True).get_text()
        except AttributeError:
            return None
        else:
            return description

    @staticmethod
    def GetProfileStatus(userId):
        response = no_data_get(f"https://www.roblox.com/users/{userId}/profile").content
        soup = BeautifulSoup(response, "html.parser")
        status = soup.find_all("div", {"class": "hidden"})[0]["data-statustext"]

        if status.strip() == "":
            status = None

        return status

    @staticmethod
    def GetAvatarImage(userId):
        response = no_data_get(f"https://www.roblox.com/users/{userId}/profile").content
        soup = BeautifulSoup(response, "html.parser")

        try:
            image = soup.find("span", {"class": "avatar-card-link avatar-image-link"}).img["src"]
        except AttributeError:
            return None
        else:
            return image

    @staticmethod
    def IsBanned(userId):
        return get(f"https://users.roblox.com/v1/users/{userId}").json()["isBanned"]

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
