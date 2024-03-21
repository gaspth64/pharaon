class Mainjoueur:

    def __init__(self, cartes, position='S'):


        self.cartes=cartes
        self.position=position

    def estvide(self):
        return len(self.cartes)==0

    def trier(self):
        self.cartes.sort(key=lambda x:x.int_hauteur)

    def afficher(self):
        self.trier()
        for carte in self.cartes:
            print(carte)

    def recevoir(self, carte):
        self.cartes.append(carte)

    def rejeter(self, id_carte):
        for i in range(len(cartes)):
            if self.cartes[i].id==id_carte:
                return self.cartes.pop(i)

    def classer_hauteurs(self):
        dico={}
        for carte in self.cartes:
            dico[carte.hauteur]=[]
        for carte in self.cartes:
            dico[carte.hauteur].append(carte)
        return dico

    def classer_couleurs(self):
        dico={}
        for carte in self.cartes:
            dico[carte.couleur]=[]
        for carte in self.cartes:
            dico[carte.couleur].append(carte)
        return dico
