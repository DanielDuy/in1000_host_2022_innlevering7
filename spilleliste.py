from sang import Sang


class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def les_fil(self, filnavn):
        file = open(filnavn)
        for line in file:  # For hver linje i filen
            ny_sang = line.strip().split(';')  # Fjern mellomrom ved starten og slutten og split via ';' i en liste
            ny_sang_objekt = Sang(ny_sang[1], ny_sang[0])  # Oppretter ny Sang-objekt
            self._sanger.append(ny_sang_objekt)  # Legger den nye Sang-objektet i Spilleliste-objektet
        file.close()

    def legg_til_sang(self, ny_sang):
        self._sanger.append(ny_sang)

    def fjern_sang(self, sang):
        self._sanger.remove(sang)

    def spill_sang(self, sang):
        sang.spill()

    def spill_alle(self):
        for sang in self._sanger:  # For hver sang listen '_sanger', i Spilleliste-objektet
            sang.spill()  # Kaller på sang metoden

    def finn_sang(self, tittel):
        for sang in self._sanger:  # For hver sang listen '_sanger', i Spilleliste-objektet
            if sang.sjekk_tittel(tittel):
                return sang
        return None

    def hent_artist_utvalg(self, artistnavn):
        sanger = []
        for sang in self._sanger:  # For hver sang listen '_sanger', i Spilleliste-objektet
            if sang.sjekk_artist(artistnavn):
                sanger.append(sang)
        return sanger
