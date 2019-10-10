
def potenza(b, n):
    if (n == 0):
        return 1
    else:
        return b * potenza(b, n - 1)


b = input("Enter a base: ")
n = input("Enter a power: ")

print(potenza(int(b), int(n)))