from .utils.request import get
from typing import Optional, List


class Group:
    """
    Represents a Roblox group.
    """

    def __init__(self, group_id: int):
        """
        Construct a new group class.
        :param group_id: The Group's ID.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id)).json()

        self.name: str = response["Name"]
        self.id: int = response["Id"]

        if response["Owner"]:
            self.owner: Optional[dict] = response["Owner"]
            self.owner_name: Optional[str] = response["Owner"]["Name"]
            self.owner_id: Optional[int] = response["Owner"]["Id"]
        else:
            self.owner: Optional[dict] = None
            self.owner_name: Optional[str] = None
            self.owner_id: Optional[int] = None

        self.emblem_url: str = response["EmblemUrl"]
        self.description: str = response["Description"]
        self.roles: list = response["Roles"]


class Groups:
    @staticmethod
    def get_users_groups(user_id: int) -> List[str]:
        """
        Gets the User's group names.
        :param user_id: The User's ID.
        :return: The User's group names.
        """
        response = get("https://api.roblox.com/users/" + str(user_id) + "/groups").json()

        return [group["Name"] for group in response]

    @staticmethod
    def get_users_group_ids(user_id: int) -> List[int]:
        """
        Get the User's group IDs.
        :param user_id: The User's ID.
        :return: The User's group IDs.
        """
        response = get("https://api.roblox.com/users/" + str(user_id) + "/groups").json()

        return [group["Id"] for group in response]

    @staticmethod
    def get_group(group_id: int) -> dict:
        """
        Get a specific group's information.
        :param group_id: The Group's ID.
        :return: A dictionary of the group's information.
        """
        return get("https://api.roblox.com/groups/" + str(group_id)).json()

    @staticmethod
    def get_group_name(group_id: int) -> str:
        """
        Get a group's name.
        :param group_id: The Group's ID.
        :return: The group's name.
        """
        return get("https://api.roblox.com/groups/" + str(group_id)).json()["Name"]

    @staticmethod
    def get_group_owner(group_id: int) -> Optional[str]:
        """
        Get the name of the group's owner.
        :param group_id: The Group's ID.
        :return: The name of the group's owner. Will return None if no group owner.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id)).json()

        if response["Owner"]:
            return response["Owner"]["Name"]
        else:
            return None

    @staticmethod
    def has_owner(group_id: int) -> bool:
        """
        Check if the group has an owner.
        :param group_id: The Group's ID to check for.
        :return: True or False.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id)).json()

        if response["Owner"]:
            return True
        else:
            return False

    @staticmethod
    def get_group_description(group_id: int) -> str:
        """
        Gets description of the group.
        :param group_id: The Group's ID.
        :return: The description of the group.
        """
        return get("https://api.roblox.com/groups/" + str(group_id)).json()["Description"]

    @staticmethod
    def get_group_roles(group_id: int) -> List[dict]:
        """
        Gets the roles of the group.
        :param group_id: The Group's ID.
        :return: A list of the group's roles.
        """
        return get("https://api.roblox.com/groups/" + str(group_id)).json()["Roles"]

    @staticmethod
    def get_group_role_names(group_id: int) -> List[str]:
        """
        Gets the role names of the group.
        :param group_id: The Group's ID.
        :return: A list of the group role names.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id)).json()["Roles"]

        return [role["Name"] for role in response]

    @staticmethod
    def get_group_role_numbers(group_id: int) -> List[int]:
        """
        Gets the role numbers of the group.
        :param group_id: The Group's ID.
        :return: A list of the group role numbers.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id)).json()["Roles"]

        return [role["Rank"] for role in response]

    @staticmethod
    def has_allies(group_id: int) -> bool:
        """
        Checks if the group has allies.
        :param group_id: The Group's ID to check for.
        :return: True or False.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id) + "/allies").json()

        if response["Groups"]:
            return True
        else:
            return False

    @staticmethod
    def has_enemies(group_id: int) -> bool:
        """
        Checks if the group has enemies.
        :param group_id: The Group's ID to check for.
        :return: True or False.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id) + "/enemies").json()

        if response["Groups"]:
            return True
        else:
            return False

    @staticmethod
    def get_group_allies(group_id: int) -> dict:
        """
        Gets the allies of the group.
        :param group_id: The Group's ID.
        :return: A dictionary of the group's allies.
        """
        return get("https://api.roblox.com/groups/" + str(group_id) + "/allies").json()

    @staticmethod
    def get_group_ally_names(group_id: int) -> List[str]:
        """
        Gets the ally names of the group.
        :param group_id: The Group's ID.
        :return: A list of the ally names.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id) + "/allies").json()["Groups"]

        return [group["Name"] for group in response]

    @staticmethod
    def get_recent_ally(group_id: int) -> Optional[dict]:
        """
        Gets the recent ally of the group.
        :param group_id: The Group's ID.
        :return: A dictionary of the ally information, or None if no allies.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id) + "/allies").json()["Groups"]

        if response:
            return response[0]
        else:
            return None

    @staticmethod
    def get_group_enemies(group_id: int) -> dict:
        """
        Gets the enemies of the group.
        :param group_id: The Group's ID.
        :return: A dictionary of the group's enemies.
        """
        return get("https://api.roblox.com/groups/" + str(group_id) + "/enemies").json()

    @staticmethod
    def get_group_enemy_names(group_id: int) -> List[str]:
        """
        Gets the enemy names of the group.
        :param group_id: The Group's ID.
        :return: A list of the enemy names.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id) + "/enemies").json()["Groups"]

        return [group["Name"] for group in response]

    @staticmethod
    def get_recent_enemy(group_id: int) -> Optional[dict]:
        """
        Gets the recent enemy of the group.
        :param group_id: The Group's ID.
        :return: A dictionary of the enemy information, or None if no enemies.
        """
        response = get("https://api.roblox.com/groups/" + str(group_id) + "/enemies").json()["Groups"]

        if response:
            return response[0]
        else:
            return None
