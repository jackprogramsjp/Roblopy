from .utils.request import get

class Asset:
    ProductType = None
    AssetId = None
    ProductId = None
    Name = None
    Description = None
    AssetTypeId = None
    Creator = None
    CreatorId = None
    CreatorType = None
    Created = None
    Updated = None
    PriceInRobux = None
    Sales = None
    IsNew = None
    IsForSale = None
    IsPublicDomain = None
    IsLimited = None
    IsLimitedUnique = None

    def __init__(self, assetId):
        response = get("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(assetId)).json()

        self.ProductType = response["ProductType"]
        self.AssetId = response["AssetId"]
        self.ProductId = response["ProductId"]
        self.Name = response["Name"]
        self.Description = response["Description"]
        self.AssetTypeId = response["AssetTypeId"]
        self.Creator = response["Creator"]["Name"]
        self.CreatorId = response["Creator"]["Id"]
        self.CreatorType = response["Creator"]["CreatorType"]
        self.Created = response["Created"]
        self.Updated = response["Updated"]
        self.PriceInRobux = response["PriceInRobux"]
        self.Sales = response["Sales"]
        self.IsNew = response["IsNew"]
        self.IsForSale = response["IsForSale"]
        self.IsPublicDomain = response["IsPublicDomain"]
        self.IsLimited = response["IsLimited"]
        self.IsLimitedUnique = response["IsLimitedUnique"]

class Assets:
    @staticmethod
    def GetAsset(assetId):
        return get("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(assetId)).json()

    @staticmethod
    def UserHasAsset(userId, assetId):
        return get(
            "https://api.roblox.com/Ownership/HasAsset?userId=" + str(userId) + "&assetId=" + str(assetId)).json()

