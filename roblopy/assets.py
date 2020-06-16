from .utils.request import get


class Asset:
    """
    Represents a Roblox asset
    """
    def __init__(self, asset_id: int):
        """
        Constructs a new asset class.
        :param asset_id: The Asset's ID.
        """
        response = get("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(asset_id)).json()

        self.product_type = response["ProductType"]
        self.asset_id = response["AssetId"]
        self.product_id = response["ProductId"]
        self.name = response["Name"]
        self.description = response["Description"]
        self.asset_type_id = response["AssetTypeId"]
        self.creator = response["Creator"]["Name"]
        self.creator_id = response["Creator"]["Id"]
        self.creator_type = response["Creator"]["CreatorType"]
        self.created = response["Created"]
        self.updated = response["Updated"]
        self.price_in_robux = response["PriceInRobux"]
        self.sales = response["Sales"]
        self.is_new = response["IsNew"]
        self.is_for_sale = response["IsForSale"]
        self.is_public_domain = response["IsPublicDomain"]
        self.is_limited = response["IsLimited"]
        self.is_limited_unique = response["IsLimitedUnique"]


class Assets:
    @staticmethod
    def get_asset(asset_id: int) -> dict:
        """
        Gets the asset's information.
        :param asset_id: The Asset's ID.
        :return: A dictionary of the asset's information.
        """
        return get("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(asset_id)).json()

    @staticmethod
    def user_has_asset(user_id: int, asset_id: int) -> bool:
        """
        Checks if the User has the asset.
        :param user_id: The User's ID to check for.
        :param asset_id: The Asset's ID to check for.
        :return: True or False.
        """
        return get(
            "https://api.roblox.com/Ownership/HasAsset?userId=" + str(user_id) + "&assetId=" + str(asset_id)).json()
