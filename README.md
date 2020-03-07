# Roblopy
Roblox API built in Python.

No module is required to use Roblopy. Roblopy uses built-in python modules.

## Installation
To install Roblopy:
```
pip install roblopy
```

How to import?
```
from roblopy import [class]
```

For example:
```
from roblopy import Users
```

## Documentation

### Users

`Users.GetUsernameById(id)` - Returns the Username of the User ID.

`Users.GetIdByUsername(username)` - Returns the User ID of the Username.

`Users.CanManage(id, assetId)` - Returns true if User can manage Asset, else false.

`Users.User(username)` or `Users.UserById(id)` - Returns class of the User's ID, Username, Avatar Uri, Avatar Final, and Is Online.

## Note

I will probably not update much of this at all, because there is already pyblox (it's a great Roblox API wrapper). If you ever want to use this, you may.
