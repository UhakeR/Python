'''

pull = download
push = upload

git config --global user.name “Valentina Grassi”
git config --global user.email “grassivalentina0@gmail.com”
git config --global color.ui auto   (per l'output colorato)
git clone: cloniamo un repository esistente da un server remoto.
git init --> inizializza un repository locale
git log: fornisce l’elenco degli ultimi commit
git diff: si vede l’elenco delle modifiche apportate ai file.
git diff --stage: modifiche nella staging area.
git checkout: riportare un file modificato nella working area all’ultimo stato aggiunto alla staging area. Ripristina all’ultimo stato committato.
Es: git checkout -- hello.txt

git commit: stai scrivendo il file nel database locale.
Es: git commit nomefile
git commit -m "my first commit": Se volete evitare il commento, mettete -m seguito dal commento tra doppi apici.
git commit hash: git genera una chiave univoca, un hash. Indentifica la modifica che è stata fatta. Ogni modifica genera un hash diverso.

git pull: download
git push: lo copi. E’ ora a fruizione di tutti. Un upload.
git status: guarda come è il repository
git add/git commit: Li uso se mi accorgo che lo devo rimodificare (già committato)

printf 'hello\world\n' > hello.txt. Si chiama REDIREZIONE. Crea un file e ci scrive dentro contemporaneamente.

gitlab.com/digitaluniversitas/homerwork-grassi.git



cd ..
git clone https://gitlab.com/digitaluniversitas/homework-grassi.git
cd homework-grassi

Se sbagli:
riprendi dall’ultimo stage con checkout
riprendi dall’ultimo commit (sempre checkout)
Es:
git reset HEAD -- hello.txt: togli la tua roba sul server.

git tag: etichettare un commit.
Es: git tag -a v1.0 -m “tag v1.0”

git branch: crea un branch




'''