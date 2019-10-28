# queste 2 routine lasciale stare
def xor(a, b):
	return a ^ b

def sommaXOR(pile):
	s = 0
	for i in range(len(pile)):
		s = xor(s, pile[i])

	return s

# questa routine ti serve per l'input controllato
def getInt(msg, x, y):
	while (True):
		try:
			a = int(input(msg))
			if a >= x and a <= y:
				return a
		except ValueError as e:
			pass

'''
questo codice è di prova
s = 0
s0 = xor(s,  pile[0])
s1 = xor(s0, pile[1])
s2 = xor(s1, pile[2])
s3 = xor(s2, pile[3])

print(s3)
'''

'''
s = 0
for i in range(len(pile)):
	s = xor(s, pile[i])

print(s)
'''

# funzione che consente la mossa al giocatore di posto g (da 0 a 1, se ho 2 giocatori, da 0 a 2 se ho 3 giocatori ecc)
'''
def mossa(g):
	print(giocatori[g])
	#p = int(input('Pila: '))
	p = getInt('Pila: ', 0, 3)
	while pile[p] == 0:
		p = getInt('Pila: ', 0, 3)

	#n = int(input('Elementi da togliere: '))
	n = getInt('Elementi da togliere: ', 1, pile[p])
	pile[p] = pile[p] - n

# dice qual è la condizione di uscita
def uscita():
	s = sum(pile)
	return s == 0
'''

# funzione che stampa c asterischi
def asterischi(c):
	str = ''
	for i in range(c):
		str = str + '*'
	return str

# funzione che stampa le pile come asterischi
def stampaAsterischi(pile):
	for i in range(len(pile)):
		print(i, ':', asterischi(pile[i]))
