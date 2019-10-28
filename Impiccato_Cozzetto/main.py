f = open('parola.txt')
s = f.readline().strip()
f.close()

tentativi = len(s) - 1

# s = 'pippopluto'
s = s.upper()

'''
t = ''
for i in range(len(s)):
  t = t + '-'
'''

t = '-' * len(s)

print('La parola da indovinare è lunga', len(s), 'caratteri')
print('Hai', tentativi, 'tentativi')
print(t)

parolaTrovata = False
i = 1
while i<=tentativi and parolaTrovata == False:
    # for i in range(1, tentativi + 1):
    print('Tentativo', i)
    lettera = input('Inserisci una lettera: ')

    # prima volta che trovo la lettera
    lettera = lettera.upper()
    j = s.find(lettera)

    if j == -1:
        print('Lettera', lettera, 'non trovata')

    # trovo le altre se ci sono
    while j != -1:
        print('La lettera', lettera, 'si trova in posizione', j)
        t = t[:j] + lettera + t[j + 1:]
        # print(i)
        j = s.find(lettera, j + 1)

    print(t)

    if s == t:
        parolaTrovata = True

    i = i + 1

if parolaTrovata == False:
    print('Hai superato il numero massimo di tentativi. La parola era', s)
else:
    print('Bravo! Hai indovinato al tentativo', i - 1)
