HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        if summa < 0:  
            return False
        else:
            kortti.lataa(summa)
            return True

    def osta_lounas(self, kortti):
        if kortti.saldo < HINTA:
            return False
        else:
            kortti.osta(HINTA)
            self.myytyja_lounaita = self.myytyja_lounaita + 1
            return True