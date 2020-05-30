# gd-api
Python wrapper for the GDBrowser API, and other GD tools as well (Original API by GD Colon)
[Original GD API Documentation here](https://gdbrowser.com/api) | [Geometry Dash Tools](https://gdcolon.com/tools) 

# setup
To install the package, type the following on your console.
```pip install geomepydash```

# documentation
Open your code, and type:
```py
import gd
```
to import all of the modules from the package.

**Examples**

_All data (except GD Tools) are returned in a **class.**_
```py
import gd
level = gd.daily()
print(level.name)
# returns the current daily level name

mytextbox = gd.textbox(
  text = 'I love geometry dash!',
  name = 'My cute monster',
  color = 'blue',
  char = gd.Characters.Scratch(expression='talk')
)
print(mytextbox)
# returns the link to the image.
```
