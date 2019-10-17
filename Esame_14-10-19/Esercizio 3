from Studente import Studente
from ClasseScolastica import ClasseScolastica

from Persona import Persona
from datetime import date

#import json

def main():

  votiQ = {'latino': 8.5, 'matematica': 9, 'geografia': 6}

  classeQ = ClasseScolastica('5DI', 17, 82, 2)

  q = Studente(87727, 'Rossi', 'Riccardo', date(2003, 2, 12), 'Brescia', 'M', classeQ, votiQ)
  print(q)
  print() 

  #print(q.getCodiceFiscale())

  votiR =  {'greco': 8.5, 'matematica': 6, 'latino': 6, 'storia': 5}

  # stessa classe di q
  r = Studente(11234, 'Bianchi', 'Federica', date(2002, 6, 24), 'Torino', 'F', classeQ, votiR)
  print(r)
  print() 

  p = Persona('Cozzetto', 'Maurizio', date(1959, 4, 1), 'Roma', 'M')
  print(p)
  print() 

  s = Persona('Verdi', 'Maurizio', date(1998, 7, 12), 'Roma', 'M')
  print(s)
  print() 
  
  t = Persona('Gialli', 'Milena', date(1977, 4, 30), 'Torino', 'F')

  print('Salvataggio dati...')
  with open('persone.csv', 'w') as f:
    f.write(p.toCSV())
    f.write(s.toCSV())
    f.write(t.toCSV())

  with open('studenti.csv', 'w') as f:
    f.write(q.toCSV())
    f.write(r.toCSV())

main()
