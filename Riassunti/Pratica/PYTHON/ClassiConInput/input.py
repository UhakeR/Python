
class Persona:
    def __init__(self, nome = input('Nome: '), cognome = input('Cognome: '), sesso = input('Sesso: '), eta = input('Età: '), altezza = input('Altezza: ')):
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


