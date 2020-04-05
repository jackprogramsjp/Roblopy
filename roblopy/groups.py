from .utils.request import get

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
        response = get("https://api.roblox.com/groups/" + str(groupId)).json()

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
        response = get("https://api.roblox.com/users/" + str(userId) + "/groups").json()

        return [group["Name"] for group in response]

    @staticmethod
    def GetUsersGroupIds(userId):
        response = get("https://api.roblox.com/users/" + str(userId) + "/groups").json()

        return [group["Id"] for group in response]

    @staticmethod
    def GetGroup(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId)).json()

    @staticmethod
    def GetGroupName(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId)).json()["Name"]

    @staticmethod
    def GetGroupOwner(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId)).json()["Owner"]["Name"]

    @staticmethod
    def GetGroupDescription(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId)).json()["Description"]

    @staticmethod
    def GetGroupRoles(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId)).json()["Roles"]

    @staticmethod
    def GetGroupRoleNames(groupId):
        response = get("https://api.roblox.com/groups/" + str(groupId)).json()["Roles"]

        return [role["Name"] for role in response]

    @staticmethod
    def GetGroupRoleNumbers(groupId):
        response = get("https://api.roblox.com/groups/" + str(groupId)).json()["Roles"]

        return [role["Rank"] for role in response]

    @staticmethod
    def GetGroupAllies(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId) + "/allies").json()

    @staticmethod
    def GetGroupAllyNames(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId) + "/allies").json()["Groups"]

    @staticmethod
    def GetRecentAllyOfGroup(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId) + "/allies").json()["Groups"][0]

    @staticmethod
    def GetGroupEnemies(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId) + "/enemies").json()

    @staticmethod
    def GetGroupEnemyNames(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId) + "/enemies").json()["Groups"]

    @staticmethod
    def GetRecentEnemyOfGroup(groupId):
        return get("https://api.roblox.com/groups/" + str(groupId) + "/enemies").json()["Groups"][0]
