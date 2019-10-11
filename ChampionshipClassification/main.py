import json

classification = {}

while True:
    teamName = ''
    while not teamName.isalpha():
        teamName = input('Team Name: ')

    teamPoint = -1
    while teamPoint < 0:
        try:
            teamPoint = int(input("Team Points: "))
        except TypeError:
            print('sei scemo')

        except ValueError:
            print('sei scemo')

    classification.update({teamName.capitalize(): teamPoint})

    it = input('vuoi continuare? ')
    if it == 'n':
        break


with open('classification.json', 'w') as c:
    c.write(json.dumps(classification, default=str))
