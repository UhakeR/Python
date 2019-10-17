def cercaContatto(codice, agenda):
    return codice in agenda.keys()


def stampaAgenda(agenda):
    for codice, contatto in agenda.items():
        print(codice, '=>', contatto)


def aggiungiModificaContatto(codice, nome, telefoni, agenda):
    agenda[codice] = [codice, nome, telefoni]


def eliminaContatto(codice, agenda):
    del (agenda[codice])


def caricaAgenda(agenda, nomeFile):
    with open(nomeFile, 'r') as f:
        for line in f:
            line = line.rstrip()
            # print(line)
            tok = line.split(';')
            # print(tok)
            agenda[tok[0]] = tok


def salvaAgenda(agenda, nomeFile):
    with open(nomeFile, 'w') as f:
        for v in agenda.values():
            f.write(v[0] + ';' + v[1] + ';' + v[2] + '\n')


def main():
    agenda = {}
    print('Caricamento dati...')
    caricaAgenda(agenda, 'Rubrica.txt')

    finito = False
    while not finito:

        print('1. Stampa agenda')
        print('2. Cerca contatto')
        print('3. Aggiungi nuovo contatto')
        print('4. Modifica contatto')
        print('5. Elimina contatto')
        print('6. Esci dal programma')

        scelta = input('Inserisci scelta: ')

        if scelta == '1':
            print('Stampa agenda')
            stampaAgenda(agenda)

        elif scelta == '2':
            print('Cerca contatto')
            codice = input('Codice: ')
            trovato = cercaContatto(codice, agenda)

            if not trovato:
                print('Il contatto non esiste al momento')
            else:
                print('Contatto trovato')
                print(agenda[codice])

        elif scelta == '3':
            print('Aggiungi nuovo contatto')
            codice = input('Codice: ')
            trovato = cercaContatto(codice, agenda)

            if not trovato:
                nome = input('Nome: ')
                telefoni = input('Telefoni: ')
                aggiungiModificaContatto(codice, nome, telefoni, agenda)
            else:
                print('Contatto già esistente')

        elif scelta == '4':
            print('Modifica contatto')

            codice = input('Codice: ')
            trovato = cercaContatto(codice, agenda)

            if trovato:
                nuovoNome = input('Nuovo nome: ')
                nuoviTelefoni = input('Nuovi telefoni: ')
                aggiungiModificaContatto(codice, nuovoNome, nuoviTelefoni, agenda)
            else:
                print('Il contatto non esiste')

        elif scelta == '5':
            print('Elimina contatto')
            codice = input('Codice: ')
            trovato = cercaContatto(codice, agenda)

            if trovato:
                eliminaContatto(codice, agenda)
                print('Contatto eliminato')
            else:
                print('Il contatto non esiste')

        elif scelta == '6':
            print('Esco dal programma')
            print('Salvataggio dati...')
            salvaAgenda(agenda, 'Rubrica.txt')
            finito = True


main()

