'''

== è l’uguaglianza
= è l’assegnazione

Accesso sequenziale ≠ accesso diretto
Items per definizione è una coppia di valori.

Le sequence sono di 4 tipi in Python. Tutto è modificabile tranne le tuple.
SEQUENCE :

    STRINGHE : Puoi modificarle ma implica che vengano distrutte e ricreate da capo.
    Es: stringa = 'digital'
    Si scrivono tra apici.

    LISTE : mutabili sia come grandezza sia come contenuto, normalmente omogenee, sono sequenze di oggetti variabili.
    Es: parole = [digital, universitas, master, programmazione]
    Si scrivono tra parentesi quadre.

    TUPLE : sequenze di oggetti immutabili.
    Es: mesi = (gennaio, febbraio, marzo)
    Si scrivono tra parentesi tonde.

    DIZIONARI : mi permette di connettere pezzi di informazione. Accesso diretto, accoppiamenti come chiave-valore. Anche: mappa.
    Es: alieno = {'colore': 'verde', 'punti': 5}
    Si scrivono tra parentesi graffe.

    Se voglio sapere qual è il valore di un dizionario:
    print(dizionario['chiave'])

    oppure:

    dizionario_chiave = dizionario.get('chiave')

    Es: se voglio sapere il colore di alieno:
    print(alieno['colore'])
    oppure
    alieno_colore = alieno.get('colore')

JSON : Struttura di informazioni (formattazione) che divide.

FUNZIONE : può prendere N input e restituisce un unico input.

PROCEDURA : Prende N input e non restituisce output.

Le FUNZIONI restituiscono un valore, le PROCEDURE nulla.
Se il def non ha un return, è una procedura.

ARRAY : struttura dati complessa, statica e omogenea.

LISTA: Serie di oggetti in un ordine particolare. Hai l’accesso agli oggetti tramite un indice o attraverso un loop.
Se l’indice è -, si inizia dalla fine. Es: -1 è l’ultimo elemento.


ALGORITMO : sequenza di passi. Le tre azioni fondamentali in un algoritmo sono : sequenza, selezione, iterazione.

{} = placeholder (segnaposto)

Ricerca di un valore può essere linera o dicotomica

ALIAS : altro modo di chiamare qualcosa.

* : serve per indicare tutti gli elementi. Esempio: from pizza import *

DEBUG : Serve allo sviluppatore per individuare gli errori punto per punto.
BREAK POINT : Punto in cui il codice si deve fermare. (tasto dx, debug invece di run).
ECCEZIONI : Modalità con cui vengono gestiti gli errori. Quando crasha un’app è per via di un errore non gestito.



'''