"""
geomepydash: Geometry Dash API Wrapper
-----------------
A python wrapper for GDBrowser API and GD Tools.
(c) 2020 vierofernando
"""

__title__ = 'geomepydash'
__author__ = 'vierofernando'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 vierofernando'
__version__ = '0.2.3'

from urllib.request import urlopen as fetchapi
import json
import characters
import gd
import classes