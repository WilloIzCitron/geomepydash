"""
geomepydash
~~~~~~~~~~~~~~~~~~~
GDBrowser API wrapper and GD Tools generator.
Originally made by GD Colon. For Geometry dash (game), all rights to RobTop Games.
(c) 2020 vierofernando
"""

__title__ = 'gd'
__author__ = 'vierofernando'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 vierofernando'
__version__ = '0.3.5'

def classify(obj):
    total = 'class Level:\n\t'
    for i in range(0, len(list(obj.keys()))):
        total += list(obj.keys())[i]+' = obj[\''+str(list(obj.keys())[i])+'\']\n\t'
    return total

def GDClass(obj):
    class Result:
        pass
    for i in range(0, len(list(obj.keys()))):
        toexe = 'Result.'+list(obj.keys())[i]+' = obj["'+list(obj.keys())[i]+'"]'
        exec(toexe)
    return Result

from urllib.request import urlopen as fetchapi
import json

class Characters:
    def Gatekeeper(expression):
        if expression=='dark':
            return '&char=gatekeeper.dark'
        else:
            return '&char=gatekeeper'
    def Keymaster(expression):
        if expression=='huh':
            return '&char=keymaster.huh'
        elif expression=='scared':
            return '&char=keymaster.scared'
        elif expression=='scream':
            return '&char=keymaster.scream'
        else:
            return '&char=keymaster' 
    def Monster(expression):
        if expression=='eyes':
            return '&char=monster.eyes'
        else:
            return '&char=monster'
    def Potbor(expression):
        if expression=='annoyed':
            return '&char=potbor.'+str(expression)
        elif expression=='huh':
            return '&char=potbor.'+str(expression)
        elif expression=='mad':
            return '&char=potbor.'+str(expression)
        elif expression=='right':
            return '&char=potbor.'+str(expression)
        elif expression=='talk':
            return '&char=potbor.'+str(expression)
        elif expression=='tired':
            return '&char=potbor.'+str(expression)
        else:
            return '&char=potbor'
    def Scratch(expression):
        if expression=='annoyed':
            return '&char=scratch.'+str(expression)
        elif expression=='huh':
            return '&char=scratch.'+str(expression)
        elif expression=='mad':
            return '&char=scratch.'+str(expression)
        elif expression=='right':
            return '&char=scratch.'+str(expression)
        elif expression=='talk':
            return '&char=scratch.'+str(expression)
        elif expression=='tired':
            return '&char=scratch.'+str(expression)
        else:
            return '&char=scratch'
    def Shopkeeper(expression):
        if expression=='annoyed':
            return '&char=shopkeeper.annoyed'
        else:
            return '&char=shopkeeper'
    def Spooky():
        return '&char=spooky'
    def Custom(link):
        return '&url='+str(link)+'&resize=1'
def daily():
    data = json.loads(fetchapi('https://gdbrowser.com/api/level/daily').read())
    total = {}
    for i in range(0, len(list(data.keys()))):
        if list(data.keys())[i]=='data':
            break
        total[list(data.keys())[i]] = data[list(data.keys())[i]]
    total = GDClass(total)
    return total

def weekly():
    data = json.loads(fetchapi('https://gdbrowser.com/api/level/weekly').read())
    total = {}
    for i in range(0, len(list(data.keys()))):
        if list(data.keys())[i]=='data':
            break
        total[list(data.keys())[i]] = data[list(data.keys())[i]]
    total = GDClass(total)
    return total

def fetchProfile(inputs):
    data = json.loads(fetchapi('https://gdbrowser.com/api/profile/'+str(inputs)).read())
    try:
        temp = data.keys()
    except AttributeError:
        raise ConnectionRefusedError('User not found!')
    total = GDClass(total)
    return total

def fetchLevel(levelid):
    data = json.loads(fetchapi('https://gdbrowser.com/api/level/'+str(levelid)).read())
    total = {}
    try:
        for i in range(0, len(list(data.keys()))):
            if list(data.keys())[i]=='data':
                break
            total[list(data.keys())[i]] = data[list(data.keys())[i]]
        total = GDClass(total)
        return total
    except AttributeError:
        raise ConnectionRefusedError('Level not found!')

class Comments:
    def getFromLevel(levelid):
        if str(levelid).isnumeric()==False:
            raise ValueError('Parameters must be Level ID. (In an integer form)')
        try:
            data = json.loads(fetchapi('https://gdbrowser.com/api/comments/'+str(levelid)+'?top').read())
            total = []
            for a in range(0, len(data)):
                total.append(GDClass(data[a]))
            return total
        except:
            raise ConnectionRefusedError('Invalid Level ID.')
    
    def getFromUser(userid):
        if str(userid).isnumeric()==False:
            raise ValueError('Parameters (user ID) must be integer value.')
        try:
            data = json.loads(fetchapi('https://gdbrowser.com/api/comments/'+str(userid)+'?type=commentHistory').read())
            total = []
            for a in range(0, len(data)):
                total.append(GDClass(data[a]))
            return total
        except:
            raise ConnectionRefusedError('Invalid User ID.')
    
    def getProfilePosts(userid):
        if str(userid).isnumeric()==False:
            raise ValueError('Parameters (user ID) must be integer value.')
        try:
            data = json.loads(fetchapi('https://gdbrowser.com/api/comments/'+str(userid)+'?type=profile').read())
            total = []
            for a in range(0, len(data)):
                total.append(GDClass(data[a]))
            return total
        except:
            raise ConnectionRefusedError('Invalid User ID.')

def levelSearch(query):
    data = json.loads(fetchapi('https://gdbrowser.com/api/search/'+str(query).replace(' ', '%20')).read())
    try:
        total = []
        for a in range(0, len(data)):
            total.append(GDClass(data[a]))
    except:
        raise ConnectionRefusedError('Level not found')
    return total

class Leaderboard:
    def topPlayers(count):
        if count>5000:
            raise OverflowError('Too many!')
        else:
            data = json.loads(fetchapi('https://gdbrowser.com/api/leaderboard?count='+str(count)).read())
            try:
                total = []
                for a in range(0, len(data)):
                    total.append(GDClass(data[a]))
            except:
                raise ConnectionRefusedError('Invalid Query')
            return total
    def topCreators(count):
        if count>5000:
            raise OverflowError('Too many!')
        else:
            data = json.loads(fetchapi('https://gdbrowser.com/api/leaderboard?creator&count='+str(count)).read())
            try:
                total = []
                for a in range(0, len(data)):
                    total.append(GDClass(data[a]))
            except:
                raise ConnectionRefusedError('Invalid Query')
            return total
def analyze(levelid):
    if str(levelid).isnumeric()==False:
        raise ValueError('Requires level ID, not level name')
    else:
        data = json.loads(fetchapi('https://gdbrowser.com/api/analyze/'+str(levelid)).read())
        total = GDClass(data)
        return total

def icon(name, *args, **kwargs):
    form = '&form='+str(kwargs.get('form', None))
    size = '&size='+str(kwargs.get('size', None))
    if size==None:
        size = ''
    else:
        if str(size).isnumeric()==False:
            raise ValueError('Size must be a number')
    if form==None:
        form = ''
    return 'https://gdbrowser.com/icon/'+str(name)+str(form)+str(size)
    

def logo(text):
    return 'https://gdcolon.com/tools/gdlogo/img/'+str(text).replace(' ', '%20')
def text(text ,font, *args, **kwargs):
    hexcol = '&color='+str(kwargs.get('color', None))
    if hexcol==None:
        hexcol = ''
    return 'https://gdcolon.com/tools/gdfont/img/'+str(text).replace(' ', '%20')+'?font='+str(font)+str(hexcol)
def comment(text, author, *args, **kwargs):
    text = str(text).replace(' ', '%20')
    author = str(author).replace(' ', '%20')
    likes = '&likes='+str(kwargs.get('likes', None))
    color = '&color='+str(kwargs.get('color', None))
    if kwargs.get('likes', None)==None:
        likes = '&likes=0'
    if kwargs.get('color', None)==None:
        color = ''
    mod = '&mod='+str(kwargs.get('mod', None))
    if kwargs.get('mod', None)==None:
        mod = ''
    uhd = ''
    if kwargs.get('uhd', None)==True:
        uhd = '&uhd'
    deletable = ''
    if kwargs.get('deletable', None)==True:
        deletable = '&deletable'
    return 'https://gdcolon.com/tools/gdcomment/img/'+str(text)+'?name='+str(author)+str(likes)+str(color)+str(mod)+str(uhd)+str(deletable)
def textbox(text, name, color, char, *args, **kwargs):
    text = str(text).replace(' ', '%20')
    name = str(name).replace(' ', '%20')
    color = '&color='+str(kwargs.get('color', None))
    mobile = ''
    if kwargs.get('mobile', None)==True:
        mobile = '&oldfont'
    if kwargs.get('color', None)==None:
        color = ''
    return 'https://gdcolon.com/tools/gdtextbox/img/'+str(text)+'?name='+str(name)+str(color)+str(char)