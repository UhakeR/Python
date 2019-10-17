import json

ranking = {}
pairScore = 1
winnerScore = 3
loserScore = 0
team01 = ''


def main():
    with open('ranking.json', 'r') as f:  # apre il file "ranking.json" per aggiornarlo
        ranking = json.load(f)
        print(ranking)  # debug: dizionario "ranking" di Python importato correttamente?


    while True:  # while-loop qui per inserire più partite e terminare con 'q'
        team01 = str(input("Type the name of the 1st team ('q' to quit): "))  # inserisce una partita di team01 e team02 con i relativi goals
        if team01 == 'q':
            break
        team01 = team01.capitalize()
        try:
            goal01 = int(input("Type the no. of goals made by the 1st team: "))
            if goal01<0:  # controllo no gol negativi
                print("Not negative numbers of goals!")
                break
        except ValueError:
            print("It should be a number of goals!")
            break


        team02 = str(input("Type the name of the 2nd team ('q' to quit): "))
        if team02 == 'q':
            break
        team02 = team02.capitalize()
        try:
            goal02 = int(input("Type the no. of goals made by the 2nd team: "))
            if goal02<0:  # controllo no. gol negativi
                print("Not negative numbers of goals!")
                break
        except ValueError:
            print("It should be a number of goals!")
            break

# equal result
        if goal01 == goal02:  # verifica il pareggio
            print("equal result")  # scrive 1 punto per ogni team nel dizionario "rankig"
            if team01 in ranking:  # check if key exists: se esiste già team01
                ranking[team01] = ranking[team01] + pairScore  # pareggio
            else:
                ranking[team01.capitalize()] = pairScore  # nuovo team01

            if team02 in ranking:  # check if key exists: se esiste già team02
                ranking[team02] = ranking[team02] + pairScore  # pareggio
            else:
                ranking[team02.capitalize()] = pairScore  # nuovo team vincitore

# team 01 is the winner
        elif goal01>goal02:  # verifica se team01 è vincitore
            print(team01, " is the winner")  # debug: scrive il  vincitore
            if team01 in ranking:  # check if key exists: se esiste già team01
                ranking[team01] = ranking[team01] + winnerScore  # vittoria
            else:
                ranking[team01] = winnerScore  # nuovo team01
            if team02 in ranking:  # check if key exists: se esiste già team02
                ranking[team02] = ranking[team02] + loserScore  # sconfitta

#team 02 is the winner
        else:
            print(team02.capitalize(), "is the winner")
            if team02 in ranking:  # check if key exists: se esiste già team02
                ranking[team02] = ranking[team02] + winnerScore  # vittoria
            else:
                ranking[team02] = winnerScore  # nuovo team02 sconfitto
            if team01 in ranking:  # check if key exists: se esiste già team01
                ranking[team01] = ranking[team01] + loserScore  # sconfitta
            else:
                ranking[team01] = loserScore  # nuovo team01

        print(ranking)  # debug

        with open('ranking.json', 'w') as jRanking:  # sovrascrivo il dizionario "ranking" nel file JSON
            json.dump(ranking, jRanking)


main()