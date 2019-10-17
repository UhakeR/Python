import csv


def autoriPerBrano(nomefile, titolo):
    with open(nomefile, encoding='utf-8') as f:
        # Creo un oggetto reader
        reader = csv.reader(f, delimiter=';')

        # Mi faccio dare i brani
        brani = list(reader)

        for i in range(1, len(brani)):
            if titolo == brani[i][1]:
                return brani[i][5]

        return None


def elencoBraniPerAlbum(nomefile, titolo):
    with open(nomefile) as f:
        titoliBrani = []

        # Creo un oggetto reader
        reader = csv.reader(f, delimiter=';')

        # Mi faccio dare i brani
        brani = list(reader)

        # for i in range(1, len(brani)):
        #  if brani[i][3] == titolo:
        #            titoliBrani.append(brani[i][1])

        # LC, List Comprehension, Pythonic Way :-)
        titoliBrani = [brani[i][1] for i in range(1, len(brani)) if brani[i][3] == titolo]

        return titoliBrani


def conteggioBraniPerGenere(nomefile, genere):
    with open(nomefile) as f:

        conteggio = 0

        # Creo un oggetto reader
        reader = csv.reader(f, delimiter=';')

        # Mi faccio dare i brani
        brani = list(reader)

        for i in range(1, len(brani)):
            if brani[i][0] == genere:
                conteggio = conteggio + 1

        return conteggio


def conteggioBraniPerArtista(nomefile, artista):
    with open(nomefile) as f:

        conteggio = 0

        # Creo un oggetto reader
        reader = csv.reader(f, delimiter=';')

        # Mi faccio dare i brani
        brani = list(reader)

        for i in range(1, len(brani)):
            if brani[i][4] == artista:
                conteggio = conteggio + 1

        return conteggio


def conteggioBraniPerOgniGenere(nomefile):
    with open(nomefile) as f:

        # Creo un oggetto reader
        reader = csv.reader(f, delimiter=';')

        # Mi faccio dare i brani
        brani = list(reader)

        # creo un dizionario genere => conteggio brani di quel genere
        generi = {}

        for i in range(1, len(brani)):
            if brani[i][0] not in generi:
                generi[brani[i][0]] = 1
            else:
                generi[brani[i][0]] = generi[brani[i][0]] + 1

        # generi = {generi[brani[i][0]] = 1 if brani[i][0] not in generi else generi[brani[i][0]] = generi[brani[i][0]] + 1 for i in range(1, len(brani))}

        return generi


def genereMaggiorNumeroDiBrani():
    generi = conteggioBraniPerOgniGenere('BraniMusicali.csv')

    maxNumeroBrani = max(list(generi.values()))

    for k, v in generi.items():
        if v == maxNumeroBrani:
            return k

    return None


def main():
    print('Conteggio brani di Jazz:', conteggioBraniPerGenere('BraniMusicali.csv', 'Jazz'))
    print()

    print('Conteggio brani degli Iron Maiden:', conteggioBraniPerArtista('BraniMusicali.csv', 'Iron Maiden'))
    print()

    print('Elenco brani dell\'album A Matter of Life and Death:',
          elencoBraniPerAlbum('BraniMusicali.csv', 'A Matter of Life and Death'))
    print()

    print('Conteggio brani per ogni genere:', conteggioBraniPerOgniGenere('BraniMusicali.csv'))
    print()

    print('Il genere col maggior numero di brani è', genereMaggiorNumeroDiBrani())


main()