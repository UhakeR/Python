
class Persona:

    def __init__(self, nome, cognome, sesso, eta, altezza):
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.eta = eta
        self.altezza = altezza

    # stampa gli attributi

    def __str__(self):
        return "Il nome è " + self.nome + ' e il cognome è ' + self.cognome + '.' + '\nIl sesso è ' + self.sesso + ' e l\'età è ' + str(self.eta) + '.\nL\'altezza è ' + str(self.altezza) + '.'

    def nomeCognome(self):
        return self.nome + ' ' + self.cognome

    def controllosesso(self):
        if self.sesso == 'Maschio':
            return 'L\'utente è ' + self.sesso

        else:
            return 'L\'utente è ' + self.sesso