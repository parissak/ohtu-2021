KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.lukujoukko = list([0] * KAPASITEETTI)
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetti ei voi olla < 0 tai muu kuin kokonaisluku")
        else:
            self.lukujoukko = list([0] * kapasiteetti)

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoko ei voi olla < 0 tai muu kuin kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.alkioiden_lkm = 0

    def kuuluu(self, haettava_luku):
        for i in range(0, self.alkioiden_lkm):
            if haettava_luku == self.lukujoukko[i]:
                return True
        return False

    def lisaa(self, lisattava_luku):
        if not self.kuuluu(lisattava_luku):
            self.lukujoukko[self.alkioiden_lkm] = lisattava_luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm >= len(self.lukujoukko):
                self.kasvata_taulukkoa()

            return True
        return False

    def poista(self, poistettava_luku):
        for i in range(0, self.alkioiden_lkm):
            if poistettava_luku == self.lukujoukko[i]:
                self.lukujoukko[i] = 0

                for j in range(i, self.alkioiden_lkm - 1):
                    apu = self.lukujoukko[j]
                    self.lukujoukko[j] = self.lukujoukko[j + 1]
                    self.lukujoukko[j + 1] = apu
                
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True
        return False

    def kasvata_taulukkoa(self):
        taulukko_uusi = [0] * (self.alkioiden_lkm + self.kasvatuskoko)

        for i in range(0, len(self.lukujoukko)):
            taulukko_uusi[i] = self.lukujoukko[i]
        
        self.lukujoukko = taulukko_uusi
    
    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujoukko[i]

        return taulu
    
    def operaatio(a, b, komento):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        if komento == "yhdiste":
            for i in range(0, len(a_taulu)):
                joukko.lisaa(a_taulu[i])
            for i in range(0, len(b_taulu)):
                joukko.lisaa(b_taulu[i])

        if komento == "leikkaus":
            for i in range(0, len(a_taulu)):
                for j in range(0, len(b_taulu)):
                    if a_taulu[i] == b_taulu[j]:
                        joukko.lisaa(b_taulu[j])

        if komento == "erotus":
            for i in range(0, len(a_taulu)):
                joukko.lisaa(a_taulu[i])
            for i in range(0, len(b_taulu)):
                joukko.poista(b_taulu[i])

        return joukko    

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko.operaatio(a, b, "yhdiste")
        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko.operaatio(a, b, "leikkaus")
        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko.operaatio(a, b, "erotus")
        return joukko
    
    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            merkkijono = ', '.join(str(e) for e in self.lukujoukko[0:self.alkioiden_lkm])
            merkkijono = "{" + merkkijono + "}"
            return merkkijono