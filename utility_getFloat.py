# questa routine ti serve per l'input controllato, Es. nell'esercizio di calcolo della media di voti

def getFloat(msg, x, y):
	while (True):
		try:
			a = float(input(msg))
			if a >= x and a <= y:
				return a
		except ValueError:
			pass
