# gd-api
Python wrapper for the GDBrowser API, and other GD tools as well (Original API by GD Colon)
[Original GD API Documentation here](https://gdbrowser.com/api) | [Geometry Dash Tools](https://gdcolon.com/tools) 

# setup
To install the package, type the following on your console.
```pip install geomepydash```

# documentation
Open your code, and type:
```import gd```
to import all of the modules from the package.

**Example: Fetch the current GD Daily level**
_All data are returned in a **class.**_
```import gd
level = gd.daily()
print(level.name)
# returns the current daily level name```
