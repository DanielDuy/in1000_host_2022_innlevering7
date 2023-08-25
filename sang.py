# Oppgave 2
class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):
        print('Spiller \'' + self._artist + '\' av \'' + self._tittel + '\'')

    def sjekk_artist(self, navn):
        a = navn.split()
        b = self._artist.split()
        for x in a:
           for y in b:
               if x == y:
                   return True
        return False

    def sjekk_tittel(self, tittel):
        input_tittel = tittel.lower()
        kopi_tittel = self._tittel.lower()
        if input_tittel == kopi_tittel:
            return True
        return False

    def sjekk_artist_og_tittel(self, artist, tittel):
        if self.sjekk_artist(artist) and self.sjekk_tittel(tittel):  # Kaller på to metoder etterpå
            return True
        return False
