

def palindromo(stringa1 = input('Inserisci una parola: ')):
    stringa2 = stringa1[::-1]

    if stringa2 == stringa1:
        return 'È un palindromo'
    else:
        return 'Non è un palindromo'


print(palindromo())