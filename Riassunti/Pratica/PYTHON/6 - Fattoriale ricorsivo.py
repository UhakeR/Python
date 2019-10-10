
def fatt(n):

    if(n == 0):
        return 1

    else:
        return n*fatt(n - 1)

f = input('Enter a number: ')

print(fatt(int(f)))