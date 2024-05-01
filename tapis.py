class Tapis:
    def __init__(self, contenu=[]):
        self.contenu = contenu

    def est_vide(self):
        return self.contenu==[]

    def empile(self,x):
        self.contenu.append(x)

    def depile(self):
        assert self.contenu != [], "tapis vide"
        return self.contenu.pop()

    def get_premiere(self):
        return self.contenu[-1]

    def afficher(self):
        assert self.contenu != [], "tapis vide"
        return f'Haut du tapis : {self.contenu[-1]}'

if __name__=='__main__':
    t = Tapis()
    t.empile('atchoum')
    t.empile(23)
    t.empile([24,23])
    t.affiche()
    a = t.depile()
    b = t.get_premiere()
    t.affiche()


