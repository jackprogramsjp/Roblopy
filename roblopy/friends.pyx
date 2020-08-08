from .utils.request import get
from typing import List


class Friends:
    @staticmethod
    def get_friends(user_id: int) -> List[dict]:
        """
        Gets the friends of the user.
        :param user_id: The User's ID.
        :return: A list of the User's friends.
        """
        return get("https://api.roblox.com/users/" + str(user_id) + "/friends").json()

    @staticmethod
    def has_friends(user_id: int) -> bool:
        """
        Checks if the User has friends.
        :param user_id: The User's ID to check for.
        :return: True or False.
        """
        response = get("https://api.roblox.com/users/" + str(user_id) + "/friends").json()

        if response:
            return True
        else:
            return False

    @staticmethod
    def get_first_friend(user_id: int) -> dict:
        """
        Gets the first friend of the user.
        :param user_id: The User's ID.
        :return: A dictionary of the friend's information.
        """
        return get("https://api.roblox.com/users/" + str(user_id) + "/friends").json()[-1]

    @staticmethod
    def get_recent_friend(user_id: int) -> dict:
        """
        Gets the recent friend of the user.
        :param user_id: The User's ID.
        :return: A dictionary of the friend's information.
        """
        return get("https://api.roblox.com/users/" + str(user_id) + "/friends").json()[0]

    @staticmethod
    def users_are_friends(user_id_1: int, user_id_2: int) -> bool:
        """
        Checks if two users are friends.
        :param user_id_1: The first User's ID to check for.
        :param user_id_2: The second User's ID to check for.
        :return: True or False.
        """
        response1 = get("https://api.roblox.com/users/" + str(user_id_1) + "/friends").json()
        response2 = get("https://api.roblox.com/users/" + str(user_id_2) + "/friends").json()
        friends_list = [user_id_1, user_id_2]
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
