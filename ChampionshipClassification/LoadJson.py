import json

def loadJson():
    b = {}
    with open('classification.json', 'r') as rjs:
        arrey=json.load(rjs)
        for kays, values in arrey.items():
            b.update({kays: values})
    return b
