# Trivial Pursuit

# le domande con le possibili risposte sono questa volta sul file quiz.txt
q = {}  # dizionario che memorizza domande (chiavi) e risposte (valori)

with open('quiz.txt') as f:
    f.readline()
    for line in f:
        line = line.rstrip()
        # print(line)
        tokens = line.split(',')
        # print(tokens)
        # print(tokens[0])

        res = [tokens[i] for i in range(1, len(tokens))]
        # print(res)
        q[tokens[0]] = res
        print('res =', res)

# print(q)

d = list(q.keys())  # le domande
r = list(q.values())  # le risposte
# print(d, r)

score = 0  # punteggio dell'utente

for i, x in enumerate(d):
    print('Domanda {}: {}'.format(i + 1, x))
    print('Risposte possibili:')

    for i in range(len(q.get(x)) - 1):
        print('{}. {}'.format(chr(65 + i), q.get(x)[i]))

    u = input('Scelta (A oppure B oppure C ecc): ').upper()
    if u == q.get(x)[-1]:
        score = score + 1

if score == 1:
    print('Hai indovinato {} risposta su {}'.format(score, len(q)))
elif score>1 and score<len(q):
    print('Hai indovinato {} risposte su {}'.format(score, len(q)))
elif score == len(d):
    print('Sei un vero campione! Le hai indovinate tutte')
else:
    print('Non hai indovinato nessuna risposta, molto male!')

for i in range(len(r)):
    # print('Risposta corretta Domanda {}: {}'.format(i + 1, r[i][-1]))
    print(f'Risposta corretta Domanda {i + 1}: {r[i][-1]}')


