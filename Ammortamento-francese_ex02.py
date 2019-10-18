# Gianluca

capital = int(input("Type the capital in euros you want to request: ")) # inserisci il capitale iniziale in euro
interestRate = float(input("Type the annual interest rate %: "))/100 # inserisci la percentuale di interesse
numberOfmonthlyPayment = int(input ("Type the number of monthly payments: ")) # inserisci il numero di rate del mutuo
interestMonthlyRate= interestRate/12 # tasso mensile (per calcolo rata fissa)

payment = (1 + 1 / ((1 + interestMonthlyRate) ** numberOfmonthlyPayment - 1)) * interestMonthlyRate * capital # calcolo rata (fissa)
print(payment)

for i in range(1, numberOfmonthlyPayment +1):
    interestComponent = interestMonthlyRate * capital # calcolo quota interessi sul capitale residuo
    # print(interestComponent) # debug
    capitalComponent = payment - interestComponent # calcolo quota capitale = rata - quota interessi
    # print(payment == interestComponent + capitalComponent) # debug per verifica che rata = = quota interessi + quota capitale
    capital = capital - capitalComponent # capitale residuo dopo ogni rata
    print(i, "\t {0:.2f}".format(capital), "\t {0:.2f}".format(interestRate*100), "\t{0:.2f}".format(interestComponent), "\t{0:.2f}".format(capitalComponent), "\t{0:.2f}".format(payment))


"""
print("N \t I \t\t\t  M \n ------------------------")
for d in range(1, yearsDuration +1): # calcola anno per anno gli interessi ed il capitale
    extraMoneyReturned = capital * interestRate / 100 # aggiungo gli interessi ogni anno: interessi = capitale * tasso / 100
        # print("The extra-money returned after", yearsDuration, "year will be: ", extraMoneyReturned )
    capital = capital + extraMoneyReturned # il capitale l'anno successivo include gli interessi dell'anno precedente = montante
        # print("The new capital to be invested will be: ", capital)
    print(d, "\t {0:.2f}".format(extraMoneyReturned), "\t {0:.2f}".format(capital)) # stampo le righe in successione
"""
