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