from bs4 import BeautifulSoup
from .utils.request import get
from typing import Optional


class User:
    """
    Represents a Roblox user.
    """

    def __init__(self, user_id: int):
        """
        Construct a new user class.
        :param user_id: The User's ID.
        """
        response = get(f"https://users.roblox.com/v1/users/{user_id}").json()
        status = get(f"https://users.roblox.com/v1/users/{user_id}/status").json()["status"]

        self.name: str = response["name"]
        self.display_name: str = response["displayName"]
        self.id: int = response["id"]
        self.is_banned: bool = response["isBanned"]
        self.created: str = response["created"]
        self.description: str = response["description"] if response["description"] else None
        self.status: str = status if status else None


class Users:
    @staticmethod
    def get_username_from_id(user_id: int) -> str:
        """
        Gets the User's name from their User ID.
        :param user_id: The User ID.
        :return: The User's name.
        """
        return get("http://api.roblox.com/users/" + str(user_id)).json()["Username"]

    @staticmethod
    def get_id_from_username(username: str) -> int:
        """
        Gets the User's ID from their username.
        :param username: The User's name.
        :return: The User's ID.
        """
        return get("http://api.roblox.com/users/get-by-username?username=" + str(username)).json()["Id"]

    @staticmethod
    def is_in_group(user_id: int, group_id: int) -> bool:
        """
        Checks if the User is in a specific group.
        :param user_id: The User's ID to check for.
        :param group_id: The Group's ID to check for.
        :return: True or False.
        """
        response = get(f"https://api.roblox.com/users/{user_id}/groups").json()
        in_group = False

        for group in response:
            if group["Id"] == group_id:
                in_group = True
                break

        return in_group

    @staticmethod
    def get_rank_in_group(user_id: int, group_id: int) -> int:
        """
        Gets the User's rank of the specific group.
        :param user_id: The User's ID.
        :param group_id: The Group's ID.
        :return: The rank of the User in the group.
        """
        response = get(f"https://api.roblox.com/users/{user_id}/groups").json()
        rank = None

        for group in response:
            if group["Id"] == group_id:
                rank = group["Rank"]
                break

        return rank

    @staticmethod
    def get_role_in_group(user_id: int, group_id: int) -> str:
        """
        Gets the User's role of the specific group.
        :param user_id: The User's ID.
        :param group_id: The Group's ID.
        :return: The role of the User in the group.
        """
        response = get(f"https://api.roblox.com/users/{user_id}/groups").json()
        role = None

        for group in response:
            if group["Id"] == group_id:
                role = group["Role"]
                break

        return role

    @staticmethod
    def group_is_primary(user_id: int, group_id: int) -> bool:
        """
        Checks if User's specific group is primary.
        :param user_id: The User's ID to check for.
        :param group_id: The Group's ID to check for.
        :return: True or False.
        """
        response = get(f"https://api.roblox.com/users/{user_id}/groups").json()
        primary = False

        for group in response:
            if group["Id"] == group_id and group["IsPrimary"]:
                primary = True
                break

        return primary

    @staticmethod
    def get_profile_description(user_id: int) -> Optional[str]:
        """
        Gets the User's bio / description.
        :param user_id: The User's ID.
        :return: The User's bio / description, but will return None if no bio / description.
        """
        response = get(f"https://users.roblox.com/v1/users/{user_id}").json()["description"]

        if response == "":
            return None

        return response

    @staticmethod
    def get_profile_status(user_id: int) -> Optional[str]:
        """
        Gets the User's status.
        :param user_id: The User's ID.
        :return: The User's status, but will return None if no status.
        """
        response = get(f"https://users.roblox.com/v1/users/{user_id}/status").json()["status"]

        if response == "":
            return None

        return response

    # @staticmethod
    # def GetProfileDescription(userId):
    #     response = no_data_get(f"https://www.roblox.com/users/{userId}/profile").content
    #     soup = BeautifulSoup(response, "html.parser")
    #
    #     try:
    #         description = soup.find("span", {"class": "profile-about-content-text linkify"}, text=True).get_text()
    #     except AttributeError:
    #         return None
    #     else:
    #         return description
    #
    # @staticmethod
    # def GetProfileStatus(userId):
    #     response = no_data_get(f"https://www.roblox.com/users/{userId}/profile").content
    #     soup = BeautifulSoup(response, "html.parser")
    #     status = soup.find_all("div", {"class": "hidden"})[0]["data-statustext"]
    #
    #     if status.strip() == "":
    #         status = None
    #
    #     return status

    @staticmethod
    def get_avatar_image(user_id: int) -> Optional[str]:
        """
        Gets the User's avatar image.
        :param user_id: The User's ID.
        :return: The User's avatar image, but will return None if avatar image cannot be found or it doesn't exist.
        """
        response = get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format"
                       "=Png&isCircular=false")

        if response.json()["data"]:
            return response.json()["data"][0]["imageUrl"]
        else:
            return None

    @staticmethod
    def is_banned(user_id: int) -> bool:
        """
        Checks if User is banned.
        :param user_id: The User's ID to check for.
        :return: True or False.
        """
        return get(f"https://users.roblox.com/v1/users/{user_id}").json()["isBanned"]

    @staticmethod
    def is_online(user_id: int) -> bool:
        """
        Checks if User is currently online.
        :param user_id: The User's ID to check for.
        :return: True or False.
        """
        return get(f"https://api.roblox.com/users/{user_id}/onlinestatus/").json()["IsOnline"]

    @staticmethod
    def get_online_status(user_id: int) -> dict:
        """
        Get's the User's online status.
        :param user_id: The User's ID.
        :return: A dictionary of the User's online status.
        """
        return get(f"https://api.roblox.com/users/{user_id}/onlinestatus/").json()

    @staticmethod
    def can_manage_asset(user_id: int, asset_id: int) -> bool:
        """
        Checks if the User can manage a given asset.
        :param user_id: The User's ID to check for.
        :param asset_id: The Asset's ID to check for.
        :return: True or False.
        """
        return get("http://api.roblox.com/users/" + str(user_id) + "/canmanage/" + str(asset_id)).json() \
            ["CanManage"]
