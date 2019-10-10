######### WHILE

i = 0
while i < 10:
    print(i)

    i = i + 1

######### FOR

for i in range(0, 10):
    print(i)

######### WHILE TRUE

while True:
    numero = int(input('Inserisci numero: '))
    if numero > 10:
        break

######### WHILE TRUE 2

lista_nomi = []
while True:
   nome = input("inserisci nome: ")
   if nome != "quit":
       lista_nomi.append(nome)
   else:
       break
print(lista_nomi)