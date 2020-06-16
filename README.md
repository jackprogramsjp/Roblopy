# Roblopy

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

Roblox API built in Python.

Migrating from 4.5 to 5.0, we will now be using snake case to follow PEP8. We are also adding type hints and docstrings.

## Installing

Here is a simple way to install:
```
pip install roblopy
```

Here is a simple way to upgrade the package to the newest version:
```
pip install roblopy --upgrade
```

## Quick Example

```python
from roblopy import Users

user_id = Users.get_id_from_username("ROBLOX")

print("Roblox's User ID is " + str(user_id))
```

## Documentation

https://github.com/jackprogramsjp/Roblopy/wiki

## Requirements

* requests
* Beautiful Soup
