def main():
    max1 = 0
    max2 = 0
    min1 = 0
    min2 = 0

    a = int(input('Inserisci un numero: '))
    b = int(input('Inserisci un numero: '))
    c = int(input('Inserisci un numero: '))
    d = int(input('Inserisci un numero: '))

    if a > b:
        max1 = a
        min1 = b
    else:
        max1 = b
        min1 = a

    if c > d:
        max2 = c
        min2 = d
    else:
        max2 = d
        min2 = c

    if max1 > max2:
        print('massimo = ', max1)
    else:
        print('massimo = ', max2)

    if min1 < min2:
        print('minimo = ', min1)
    else:
        print('minimo = ', min2)


main()
