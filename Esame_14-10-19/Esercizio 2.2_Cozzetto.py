# calcolo della media utilizzando le funzioni rese disponibili da Python (in questo caso usiamo il modulo statistics che contiene la funzione mean, che vuol dire media appunto)

import statistics


def main():
    v = []  # array dove mettere i voti

    # ciclo di lettura dei voti
    while True:
        x = float(input('Inserisci voto (-1 per terminare): '))

        if x == -1:  # esco da qua
            break
        else:
            v.append(x)  # aggiungo i voti all'array
    try:
        print('Minimo = ', min(v))
        # i = index(v)

        # tolgo il più piccolo
        v.remove(min(v))

        print('v =', v, 'statistics.mean(v) =', statistics.mean(v))
    except ValueError as e:  # THANKS SOUMAYA!
        print('Devi inserire almeno 2 voti. Errore: ', e)


main()