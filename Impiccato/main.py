# leggo il file per assegnare la parola
f = open('impiccato.txt')
parola = f.readline()
f.close()

tentativi = len(parola) - 1  # assegno la quantità di tentativi

# creo la lista di trattini che popolo con il for
listaDiTrattini = []
for i in range(len(parola)):
    listaDiTrattini.append('-')

print('La parola da indovinare è lunga {} lettere'.format(len(parola)))
print('Hai {} tentativi'.format(tentativi))

# ciclo while che si interrompe quando il numero di tentativi è uguale a 0 o quando il giocatore dà la risposta giusta
while True:
    print('Tentativo:{}'.format(tentativi))
    lettera = input('Inserisci la lettera: ')  # chiedo in input la lettera

    # quest ciclo for per ogni lettera presente in parola assegna il rispettivo indice ad i
    for i in range(len(parola)):

        # controllo se la lettera che il giocatore ha dato in input è presente nel indice i di parola
        if lettera in parola[i]:
            listaDiTrattini[i] = lettera
            print('La lettera {} si trova alla posizione {}'.format(lettera.capitalize(), i))
            i = 0

    if lettera not in parola:
        print('{} non presente'.format(lettera.capitalize()))

    # con questo if controllo se ha indovinato la parola senza aver finito i tentativi,in tal caso finicsco il programma
    if lettera == parola:
        print('Hai vinto')
        break

    # printo i trattini
    parolaNascosta = ''.join(listaDiTrattini)
    print(parolaNascosta)

    tentativi -= 1

    # quando i tentativi è uguale a 0 controllo se ha indovinato la parola o meno
    if tentativi == 0:
        if parolaNascosta == parola:
            print('Hai vinto')
            break
        elif parolaNascosta != parola:
            print('Hai superato il numero massimo di tentativi, la parola era {}'.format(parola.capitalize()))
            break