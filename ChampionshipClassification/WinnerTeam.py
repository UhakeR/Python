import json
classifica = {}

with open('classification.json', 'r') as c:
    classifica=json.load(c)

while True:
    team1 = ''
    while team1.isalpha() != True:
        team1 = input('Team 1: ')

    team2 = ''
    while team2.isalpha() != True:
        team2 = input('Team 2: ')

    point1 = -1
    while point1 < 0:
        try:
            point1 = int(input('Team 1 points: '))
        except Exception:
            print('Retry') # modificato parola "Retray" (GG)

    point2 = -1
    while point2 < 0:
        try:
            point2 = int(input('Team 2 points: '))
        except Exception:
            print('Retry') # modificato parola "Retray" (GG)
    pros = input('vuoi continuare? ')

    if pros=='q':
        break
    else:
        print('No! tu ora ti fermi')
        break





if point1 > point2:
    try:
        classifica[team1.capitalize()] += 3
        classifica[team2.capitalize()] +=0

    except Exception:
        classifica[team1.capitalize()] = 3


elif point2 > point1:
    try:
        classifica[team2.capitalize()] += 3

    except Exception:
        classifica[team2.capitalize()] = 3


elif point1 == point2:

    try:
        classifica[team1.capitalize()] += 1
        classifica[team2.capitalize()] += 1
    except Exception:
        classifica[team1.capitalize()] = 1
        classifica[team2.capitalize()] = 1
print(classifica)

with open('classification.json', 'w')as f:
    f.write(json.dumps(classifica, default=str))