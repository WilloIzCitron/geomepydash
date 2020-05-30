from urllib.request import urlopen as fetchapi
import json
import classes
import characters

class GDBrowser:
    def daily():
        data = json.loads(fetchapi('https://gdbrowser.com/api/level/daily').read())
        total = {}
        for i in range(0, len(list(data.keys()))):
            if list(data.keys())[i]=='data':
                break
            total[list(data.keys())[i]] = data[list(data.keys())[i]]
        total = classes.GDClass(total)
        return total
    
    def weekly():
        data = json.loads(fetchapi('https://gdbrowser.com/api/level/weekly').read())
        total = {}
        for i in range(0, len(list(data.keys()))):
            if list(data.keys())[i]=='data':
                break
            total[list(data.keys())[i]] = data[list(data.keys())[i]]
        total = classes.GDClass(total)
        return total
    
    def fetchProfile(inputs):
        data = json.loads(fetchapi('https://gdbrowser.com/api/profile/'+str(inputs)).read())
        try:
            temp = data.keys()
        except AttributeError:
            raise ConnectionRefusedError('User not found!')
        total = classes.GDClass(total)
        return total
    
    def fetchLevel(levelid):
        data = json.loads(fetchapi('https://gdbrowser.com/api/level/'+str(levelid)).read())
        total = {}
        try:
            for i in range(0, len(list(data.keys()))):
                if list(data.keys())[i]=='data':
                    break
                total[list(data.keys())[i]] = data[list(data.keys())[i]]
            total = classes.GDClass(total)
            return total
        except AttributeError:
            raise ConnectionRefusedError('Level not found!')
    
    def levelSearch(query):
        data = json.loads(fetchapi('https://gdbrowser.com/api/search/'+str(query).replace(' ', '%20')).read())
        try:
            total = []
            for a in range(0, len(data)):
                total.append(classes.GDClass(data[a]))
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
                        total.append(classes.GDClass(data[a]))
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
                        total.append(classes.GDClass(data[a]))
                except:
                    raise ConnectionRefusedError('Invalid Query')
                return total
    def analyze(levelid):
        if str(levelid).isnumeric()==False:
            raise ValueError('Requires level ID, not level name')
        else:
            data = json.loads(fetchapi('https://gdbrowser.com/api/analyze/'+str(levelid)).read())
            total = classes.GDClass(data)
            return total

class GDTools:
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
            likes = ''
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
        if color not in ['blue', 'brown', 'purple']:
            raise IndexError('Invali color. Please try blue, brown, or purple')
        return 'https://gdcolon.com/tools/gdtextbox/img/'+str(text)+'?name='+str(name)+str(color)+str(char)