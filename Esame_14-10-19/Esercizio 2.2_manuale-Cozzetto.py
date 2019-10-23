# gestione manuale della media

def main():
    v = []  # array dove mettere i voti
    s = 0.0  # devo sommare i voti in s
    c = 0  # conto i voti

    # ciclo di lettura dei voti
    while True:
        try:
            x = float(input('Inserisci voto (-1 per terminare): '))
        except ValueError:  # controllo che l'input sia solo numerico (by GG)
            print("E' possibile inserire solo numeri")
            break

        if x == -1:  # esco da qua
            break

        v.append(x)  # aggiungo i voti all'array

        s = s + x
        c = c + 1

    try:
        print('Minimo = ', min(v))
        # i = index(v)

        s = s - min(v)

        # tolgo il più piccolo
        v.remove(min(v))

        c = c - 1

        # stampo v senza il minimo
        print('v =', v, 'c =', c)

        # tolgo il minimo e poi decremento di uno c
        media = s / c

        print('media = ', media)
        # THANKS TO SOUMAYA!
    except ZeroDivisionError as e:
        print('Servono almeno due numeri. Errore: ', e)
    except ValueError as e:
        print('Servono almeno 2 numeri. Errore: ', e)


main()