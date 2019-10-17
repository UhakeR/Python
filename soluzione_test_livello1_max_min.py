def main():
    a = int(input('Inserisci un numero: '))
    b = int(input('Inserisci un numero: '))
    c = int(input('Inserisci un numero: '))
    d = int(input('Inserisci un numero: '))

    maximum = a
    minimum = a

    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    if d > maximum:
        maximum = d

    if b < minimum:
        minimum = b

    if c < minimum:
        minimum = c

    if d < minimum:
        minimum = d

    print('massimo =', maximum)
    print('minimum =', minimum)


main()