import urllib
import json
import random
data = json.loads(urllib.request.urlopen('https://gdcolon.com/tools/gdname/list').read())
title = random.choice(data['combos']).split(' ')

alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
word = None
while len(title)>20:
    for i in range(0, len(data['combos'])):
        if title not in alph:
            continue
        if title=="N":
            word = random.choice(data['nouns'])
            addS = random.randint(1, 8)
            if addS>6 and not word.endswith('s') and not word.endswith('x'):
                title = word + 's'
        elif title=="A":
            word = random.choice(data['adjs'])
        elif title.startswith('V'):
            verb = random.choice(data['verbs']).split('~')
            word = verb[0]
            try:
                extra = verb[1]
            except IndexError:
                extra = ""