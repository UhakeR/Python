
#l'asterisco indica che il parametro è facoltativo

def make_pizza(size, *toppings):

    print('\nMaking a ' + size + ' pizza.')
    print('Toppings:')

    for topping in toppings:
        print('- ' + topping)

