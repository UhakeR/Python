import random
import utility

class Nim:
	def __init__(self, s, p):
		self.__s = s # numero di pile
		self.__stacks = [] # è il vettore che contiene il numero di sassi
		self.__p = p # numero di giocatori

		for i in range(self.__s):
			self.__stacks.append(random.randint(1, 10)) # questo numero è scelto a caso

		#stacks = [6, 6, 4, 2]
		#self.__players = ['Luca', 'Antonio', 'Francesco']

		# array dei giocatori
		self.__players = []

		# ogni giocatore è identificato da una lettera
		for i in range(self.__p):
			self.__players.append(chr(i + 65))


	# funzione che consente la mossa al giocatore di posto p (per es. da 0 a 1, se ho 2 giocatori, da 0 a 2 se ho 3 giocatori ecc)
	def move(self, p):
		print('Giocatore', self.__players[p])

		s = utility.getInt('Pila: ', 0, len(self.__stacks) - 1)
		while self.__stacks[s] == 0:
			s = utility.getInt('Pila: ', 0, len(self.__stacks) - 1)

		t = utility.getInt('Elementi da togliere: ', 1, self.__stacks[s])
		self.__stacks[s] = self.__stacks[s] - t

	# dice qual è la condizione di uscita
	def gameOver(self):
		a = sum(self.__stacks)
		return a == 0

	# il gioco
	def play(self):
		l = 0 # serve solo per contare
		b = True
		while b:
			#print(self.__stacks)
			utility.stampaAsterischi(self.__stacks)
			m = l % len(self.__players) #serve per alternare i vari giocatori
			'''
			# codice da usare eventualmente per giocare contro la macchina
			# funzioni computer() e umano() da scrivere
			if m == 0:
				computer(m)
			else:
				umano(m)
			'''
			# la mossa del giocatore m
			self.move(m)

			l = l + 1

			# lascia stare
			s = utility.sommaXOR(self.__stacks)
			#print('Somma XOR =', s)

			# se la condizione di uscita si verifica, ti dico chi ha vinto
			if self.gameOver():
				print('Il gioco è finito. Vince ' + self.__players[m])
				b = False


def main():
  print('Benvenuto al gioco del Nim'); nim = Nim(4, 2); nim.play()

main()