#utility da utilizzare in ogni input che richieda l'inserimento di soli valori "int" numerici
def getInt(msg, x, y):
    while (True):
        try:
            a = int(input(msg))
            if a >= x and a <= y:
                return a
        except ValueError as e:
            pass