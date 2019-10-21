# Gianluca
"""Ammortamento francese Esercizio 1
Progettare un algoritmo che visualizzi la rendita annuale di un investimento
effettuato presso la banca “Più soldi per tutti”.
La banca visualizza il piano di investimento usando il capitale iniziale in euro,
la percentuale di interesse e il numero di anni dell’investimento.
Il calcolo degli interessi si effettua tramite la seguente formula:
interessi = capitale * tasso / 100
e questi verranno sommati di anno in anno al capitale."""
import decimal

capital = int(input("Type the amount of euros you want to invest: ")) # inserisci il capitale iniziale in euro
interestRate = float(input("Type the interest rate % that 'Money for All' will return yearly: ")) # inserisci la percentuale di interesse
yearsDuration = int(input ("Type the duration of the investment: ")) # inserisci il numero di anni dell’investimento

print("N \t I \t\t\t  M \n ------------------------")
for d in range(1, yearsDuration +1): # calcola anno per anno gli interessi ed il capitale
    extraMoneyReturned = capital * interestRate / 100 # aggiungo gli interessi ogni anno: interessi = capitale * tasso / 100
        # print("The extra-money returned after", yearsDuration, "year will be: ", extraMoneyReturned )
    capital = capital + extraMoneyReturned # il capitale l'anno successivo include gli interessi dell'anno precedente = montante
        # print("The new capital to be invested will be: ", capital)
    print(d, "\t {0:.2f}".format(extraMoneyReturned), "\t {0:.2f}".format(capital)) # stampo le righe in successione

