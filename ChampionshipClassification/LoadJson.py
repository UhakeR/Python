import json

def loadJson():
    b = {}
    with open('classification.json', 'r') as rjs:
        arrey=json.load(rjs)
        for keys, values in arrey.items(): # corretto "kays" (GG)
            b.update({keys: values})
    return b
