# Federica, esame 14/10/19

    # ho sostituito a "int" il float, ed introdotto un controllo di valori numerici col try-except
while True:
    try:
        a = float (input('Enter your first number : '))
    except ValueError:  # controllo che l'input sia solo numerico
        print("Sono ammessi solo interi o decimali")
        if a<=0:
            break
    try:
        b = float (input ('Enter your second number : '))
    except ValueError:  # controllo che l'input sia solo numerico
        print("Sono ammessi solo interi o decimali")
        if b<=0:
            break
    try:
        c = float (input ('Enter your third number : '))
    except ValueError:  # controllo che l'input sia solo numerico
        print("Sono ammessi solo interi o decimali")
        if c<=0:
            break
    try:
        d = float (input('Enter your last number : '))
    except ValueError:  # controllo che l'input sia solo numerico
        print("Sono ammessi solo interi o decimali")
        if d<=0:
            break
    break
max = str("Your major number is : ")
if a > b:
  if a > c:
      if a > d:
        print(max, a)
elif b > c and b > d:
      print(max, b)
elif c > d:
  print(max, c)
else:
  print(max, d)
min = str("Your smallest number is : ")
if a < b:
  if a < c:
      if a < d:
          print(min, a)
elif b < c and b < d:
      print(min, b)
elif c < d:
  print(min, c)
else:
  print(min, d)
