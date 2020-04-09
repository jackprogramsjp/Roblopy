* Classes
  * [Users](#users)
  * [User](#user)
  * [Friends](#friends)
  * [Assets](#assets)
  * [Asset](#asset)
  * [Groups](#groups)
  * [Group](#group)
***
# Users

## Properties
* None

## Methods
* GetUsernameFromId
* GetIdFromUsername
* IsInGroup
* GetRankInGroup
* GetRoleInGroup
* GroupIsPrimary
* GetProfileDescription
* IsOnline
* GetOnlineStatus
* CanManageAsset

## Users.GetUsernameFromId
Gets the User's name from their ID

**Parameters**
* userId (String or Number)

**Returns**
* String

**Example**
```python
.GetUsernameFromId("12345")
```

## Users.GetIdFromUsername
Gets the User's ID from their name

**Parameters**
* name (String)

**Returns**
* Integer

**Example**
```python
.GetIdFromUsername("ROBLOX")
```

## Users.IsInGroup
If user is in a specific group

**Parameters**
* userId (String)
* groupId (String)

**Returns**
* Boolean

**Example**
```python
.IsInGroup("12345", "54321")
```

## Users.GetRankInGroup
Get the User's rank in a specific group

**Parameters**
* userId (String)
* groupId (String)

**Returns**
* Integer

**Example**
```python
.GetRankInGroup("12345", "54321")
```

## Users.GetRoleInGroup
Get the User's role in a specific group

**Parameters**
* userId (String)
* groupId (String)

**Returns**
* String

**Example**
```python
.GetRoleInGroup("12345", "54321")
```

## Users.GroupIsPrimary
If a specific group is the User's primary

**Parameters**
* userId (String)
* groupId (String)

**Returns**
* Boolean

**Example**
```python
.GroupIsPrimary("12345", "54321")
```

## Users.GetProfileDescription
Get the User's profile description

**Parameters**
* userId (String)

**Returns**
* String

**Example**
```python
.GetProfileDescription("12345")
```

## Users.IsOnline
If user is online currently

**Parameters**
* userId (String)

**Returns**
* Boolean

**Example**
```python
.IsOnline("12345")
```

## Users.GetOnlineStatus
Get the User's online status

**Parameters**
* userId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetOnlineStatus("12345")
```

## Users.CanManageAsset
User can manage asset

**Parameters**
* userId (String)
* assetId (String)

**Returns**
* Boolean

**Example**
```python
.CanManageAsset("12345", "12345")
```

# User

## Properties
* Id (Integer) - The User's ID.
* Username (String) - The User's Name.

## Methods
* Constructor

## User
Create a new object

**Parameters**
* userId (String)

**Returns**
* Object

**Example**
```python
User("12345")
```

# Friends

## Properties
* None

## Methods
* GetFriends
* GetFirstFriend
* GetRecentFriend
* UsersAreFriends

## Friends.GetFriends
Gets the friends of the User

**Parameters**
* userId (String)

**Returns**
* JSON Object / Python List and Dictionary

**Example**
```python
.GetFriends("12345")
```

## Friends.GetFirstFriend
Gets the first friend of the User

**Parameters**
* userId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetFirstFriend("12345")
```

## Friends.GetRecentFriend
Gets the recent friend of the User

**Parameters**
* userId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetRecentFriend("12345")
```

## Friends.UsersAreFriends
Whether the user is friends with the other user or not

**Parameters**
* userId1 (String)
* userId2 (String)

**Returns**
* Boolean

**Example**
```python
.UsersAreFriends("12345", "54321")
```

# Assets

## Properties
* None

## Methods
* GetAsset
* UserHasAsset

## Assets.GetAsset
Gets the asset information

**Parameters**
* assetId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetAsset("12345")
```

## Assets.UserHasAsset
Whether the user has a specified asset or not

**Parameters**
* userId (String)
* assetId (String)

**Returns**
* Boolean

**Example**
```python
.UserHasAsset("12345", "0246810")
```

# Asset

## Properties
* ProductType (String) - The type of product (for example: "User Product").
* AssetId (Integer) - The asset ID.
* ProductId (Integer) - The product ID.
* Name (String) - The asset name.
* Description (String) - The asset description.
* AssetTypeId (Integer) - The asset type ID.
* Creator (String) - The creator of the asset.
* CreatorId (Integer) - The creator's ID.
* CreatorType (String) - The creator's type.
* Created (String) - The date when the asset was created.
* Updated (String) - The date when the asset was recently updated.
* PriceInRobux (Integer) - The robux price of the asset.
* Sales (Integer) - The sales of the asset.
* IsNew (Boolean) - Whether the asset is new or not.
* IsForSale (Boolean) - Where the asset is for sale or not.
* IsPublicDomain (Boolean) - Whether the asset is public domain or not.
* IsLimited (Boolean) - Where the asset is a limited or not.
* IsLimitedUnique (Boolean) - Whether the asset is limited unique or not.

## Methods
* Constructor

## Asset
Create a new object

**Parameters**
* assetId (String)

**Returns**
* Object

**Example**
```python
Asset("12345")
```

# Groups

## Properties
* None

## Methods
* GetUsersGroups
* GetUsersGroupIds
* GetGroup
* GetGroupName
* GetGroupOwner
* GetGroupDescription
* GetGroupRoles
* GetGroupRoleNames
* GetGroupRoleNumbers
* GetGroupAllies
* GetGroupAllyNames
* GetRecentAllyOfGroup
* GetGroupEnemies
* GetGroupEnemyNames
* GetRecentEnemyOfGroup

## Groups.GetUsersGroups
Gets a list of the User's groups

**Parameters**
* userId (String)

**Returns**
* Python List

**Example**
```python
.GetUsersGroups("12345")
```

## Groups.GetUsersGroupIds
Gets a list of the User's groups' IDs

**Parameters**
* userId (String)

**Returns**
* Python List

**Example**
```python
.GetUsersGroupIds("12345")
```

## Groups.GetGroup
Gets the group's information

**Parameters**
* groupId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetGroup("12345")
```

## Groups.GetGroupName
Gets the group's name

**Parameters**
* groupId (String)

**Returns**
* String

**Example**
```python
.GetGroupName("12345")
```

## Groups.GetGroupOwner
Gets the group's owner

**Parameters**
* groupId (String)

**Returns**
* String

**Example**
```python
.GetGroupOwner("12345")
```

## Groups.GetGroupDescription
Gets the group's description

**Parameters**
* groupId (String)

**Returns**
* String

**Example**
```python
.GetGroupDescription("12345")
```

## Groups.GetGroupRoles
Gets the group's roles

**Parameters**
* groupId (String)

**Returns**
* JSON Object / Python List and Dictionary

**Example**
```python
.GetGroupRoles("12345")
```

## Groups.GetGroupRoleNames
Gets the group's role names

**Parameters**
* groupId (String)

**Returns**
* Python List

**Example**
```python
.GetGroupRoleNames("12345")
```

## Groups.GetGroupRoleNumbers
Gets the group's role numbers

**Parameters**
* groupId (String)

**Returns**
* Python List

**Example**
```python
.GetGroupRoleNumbers("12345")
```

## Groups.GetGroupAllies
Gets the group's allies

**Parameters**
* groupId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetGroupAllies("12345")
```

## Groups.GetGroupAllyNames
Gets the group's ally names

**Parameters**
* groupId (String)

**Returns**
* Python List

**Example**
```python
.GetGroupAllyNames("12345")
```

## Groups.GetRecentAllyOfGroup
Gets the group's recent ally

**Parameters**
* groupId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetRecentAllyOfGroup("12345")
```

## Groups.GetGroupEnemies
Gets the group's enemies

**Parameters**
* groupId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetGroupEnemies("12345")
```

## Groups.GetGroupEnemyNames
Gets the group's enemy names

**Parameters**
* groupId (String)

**Returns**
* Python List

**Example**
```python
.GetGroupEnemyNames("12345")
```

## Groups.GetRecentEnemyOfGroup
Gets the group's recent enemy

**Parameters**
* groupId (String)

**Returns**
* JSON Object / Python Dictionary

**Example**
```python
.GetRecentEnemyOfGroup("12345")
```

# Group

## Properties
* Name (String) - The group's name.
* Id (Integer) - The group's ID.
* Owner (JSON Object / Python Dictionary) - The group's owner information.
* OwnerName (String) - The group's owner name.
* OwnerId (Integer) - The group's owner ID.
* EmblemUrl (String) - The group's emblem url.
* Description (String) - The group's description.
* Roles (JSON Object / Python Dictionary) - The group's roles.

## Methods
* Constructor

## Group
Create a new object

**Parameters**
* groupId (String)

**Returns**
* Object

**Example**
```python
Group("12345")
```