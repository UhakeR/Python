# questa routine ti serve per l'input controllato
def getInt(msg, x, y):
	while (True):
		try:
			a = int(input(msg))
			if a >= x and a <= y:
				return a
		except ValueError:
			pass

def getFloat(msg, x, y):
	while (True):
		try:
			a = float(input(msg))
			if a >= x and a <= y:
				return a
		except ValueError:
			pass
