import requests

class Group:
    Name = None
    Id = None
    Owner = None
    OwnerName = None
    OwnerId = None
    EmblemUrl = None
    Description = None
    Roles = None

    def __init__(self, groupId):
        response = requests.get("https://api.roblox.com/groups/" + str(groupId)).json()

        self.Name = response["Name"]
        self.Id = response["Id"]
        self.Owner = response["Owner"]
        self.OwnerName = response["Owner"]["Name"]
        self.OwnerId = response["Owner"]["Id"]
        self.EmblemUrl = response["EmblemUrl"]
        self.Description = response["Description"]
        self.Roles = response["Roles"]

class Groups:
    @staticmethod
    def GetUsersGroups(userId):
        response = requests.get("https://api.roblox.com/users/" + str(userId) + "/groups").json()

        return [group["Name"] for group in response]

    @staticmethod
    def GetUsersGroupIds(userId):
        response = requests.get("https://api.roblox.com/users/" + str(userId) + "/groups").json()

        return [group["Id"] for group in response]

    @staticmethod
    def GetGroup(groupId):
        return requests.get("https://api.roblox.com/groups/" + str(groupId)).json()

    @staticmethod
    def GetGroupName(groupId):
        return requests.get("https://api.roblox.com/groups/" + str(groupId)).json()["Name"]

    @staticmethod
    def GetGroupOwner(groupId):
        return requests.get("https://api.roblox.com/groups/" + str(groupId)).json()["Owner"]["Name"]

    @staticmethod
    def GetGroupDescription(groupId):
        return requests.get("https://api.roblox.com/groups/" + str(groupId)).json()["Description"]

    @staticmethod
    def GetGroupRoles(groupId):
        return requests.get("https://api.roblox.com/groups/" + str(groupId)).json()["Roles"]

    @staticmethod
    def GetGroupRoleNames(groupId):
        response = requests.get("https://api.roblox.com/groups/" + str(groupId)).json()["Roles"]

        return [role["Name"] for role in response]

    @staticmethod
    def GetGroupRoleNumbers(groupId):
        response = requests.get("https://api.roblox.com/groups/" + str(groupId)).json()["Roles"]

        return [role["Rank"] for role in response]

    @staticmethod
    def GetGroupAllies(groupId):
        return requests.get("https://api.roblox.com/groups/" + str(groupId) + "/allies").json()

    @staticmethod
    def GetGroupAllyNames(groupId):
        try:
            response = requests.get("https://api.roblox.com/groups/" + str(groupId) + "/allies").json()["Groups"]
        except IndexError:
            return None
        else:
            return [ally["Name"] for ally in response]

    @staticmethod
    def GetRecentAllyOfGroup(groupId):
        try:
            response = requests.get("https://api.roblox.com/groups/" + str(groupId) + "/allies").json()["Groups"][0]
        except IndexError:
            return None
        else:
            return response

    @staticmethod
    def GetGroupEnemies(groupId):
        return requests.get("https://api.roblox.com/groups/" + str(groupId) + "/enemies").json()

    @staticmethod
    def GetGroupEnemyNames(groupId):
        try:
            response = requests.get("https://api.roblox.com/groups/" + str(groupId) + "/enemies").json()["Groups"]
        except IndexError:
            return None
        else:
            return [enemy["Name"] for enemy in response]

    @staticmethod
    def GetRecentEnemyOfGroup(groupId):
        try:
            response = requests.get("https://api.roblox.com/groups/" + str(groupId) + "/enemies").json()["Groups"][0]
        except IndexError:
            return None
        else:
            return response
