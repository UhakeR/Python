'''

Creare un file
printf " "> nomefile.txt

Quando faccio pull, quello che mi arriva è committato (o unmodified).
Quando ho editato il file, si trova in modified (non in staged).


Il CONTROLLO DI VERSIONE è un sistema che registra, nel tempo, i cambiamenti a un file o a una serie di file, così da poter richiamare
una specifica versione in un secondo momento.

Il CONTROLLO DI VERSIONE può essere:

LOCALE: è vecchio

CENTRALIZZATO: ogni utente ha una copia del codice sorgente. Il software è formato da tante directory.

DISTRIBUITO: es. Git. Abbiamo un main server, una copia locale che però sta all’interno di un piccolo server a sua volta.
Così, se va momentaneamente ko, ho salva la mia rete.

GIT è un sistema di controllo di versione distribuito, creato da Linus Torvalds nel 2005.
Serve per tenere traccia dei cambiamenti al proprio codice e per facilitare lo sviluppo condiviso.

La differenza tra Dropbox, Gdrive ecc è che oltre a quello che fa permette di tenere traccia di tutti i cambiamenti.

Ci sono 3 aree di base:

WORKING: valentina-grassi
staging: area virtuale interessata da un commit (area che tiene git che interessa tutte le modifiche che facciamo)
repository: area definitiva dove le modifiche sono state confermate

STATO DEI FILE:

UNTRACKED:
UNMODIFIED (COMMITTED): versionato ma non modificato
MODIFIED: modificato e contrassegnato
STAGED:

repository: è il sorgente sul server

Oppure git commit e nome file, e lui in automatico fa git add e git commit:
git commit nomefile

Modifica -> stage -> commmit

Se vuoi vedere le modifiche che ha fatto un altro: PULL (download di quello che l'altro ha pushato, ovvero uploadato).


Ogni commit va commentato. Bisogna capire cosa è stato fatto.

Comando add: è un comando che aggiunge anche le modifiche. Si può anche caricare un’intera directory.

Il -- tratta ogni argomento dopo questi due trattini come un nome di un file.

pull -> push
Sincronizzazione con il repository remoto
con push allineamo il repository remoto a quello locale.

Branch: linea di sviluppo separata. Quando viene creato un progetto, viene staccato un branch di sviluppo.
Non si può sviluppare altrimenti, per non fare casini.

deploy significa rilasciare
A un certo punto faccio il merging e lo incastro nella linea principale.


Differenza VERSION e RELEASE
Quando si rilascia una versione tipo 3.5. 3 è la versione, 5 è la release.

git clone serve per accedere a una repository
git add: aggiungi
git pull prende le modifiche


'''