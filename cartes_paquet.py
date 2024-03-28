import random
from constantes import *


class Carte:
    #variables de classe : correspondance hauteurs et couleurs
    #on récupère les dessins Unicode des cartes (sauf le cavalier)
    JEU_IMAGES = (tuple(chr(x) for x in range(0x1f0d1, 0x1f0df) if x != 0x1f0dc ),
                tuple(chr(x) for x in range(0x1f0c1, 0x1f0cf) if x != 0x1f0cc ),
                tuple(chr(x) for x in range(0x1f0b1, 0x1f0bf) if x != 0x1f0bc ),
                tuple(chr(x) for x in range(0x1f0a1, 0x1f0af) if x != 0x1f0ac)
                )


    def __init__(self, couleur, hauteur):
        '''
        hauteur est un str de '1' pour l'As à 'K' pour le roi
        couleur est un str entre 'c', 'd', 'h', 's'
        int_hauteur est l'entier correspondant : 0 pour l'As à 12 pour le K
        '''
        self.couleur = couleur
        self.hauteur = hauteur
        self.int_hauteur = DICO_HAUTEURS[hauteur]+1
        self.dessin = self.JEU_IMAGES[DICO_COULEURS[couleur]][DICO_HAUTEURS[hauteur]]
        self.id = couleur+hauteur
        #valeur : dépend du jeu !
        #au pharaon 1 pour l'As, 2 pour le 2, etc et 10 pour les honneurs
        #au barbu : l'As est plus fort que le Roi, plus fort que la Dame...
        #donc : 11 pour J, 12 pour Q
        #13 pour K et 14 pour As
        self.valeur = DICO_VALEURS[hauteur] # à compléter

    def __str__(self):
        #permet de faire print facilement
        return self.couleur+self.hauteur + ' ' + self.dessin


class PaquetCartes:
    def __init__(self, nb):
        self.nb_cartes = nb
        hauteur_min = 0 if nb == 52 else 6 #on commence au 7 pour un jeu de 32
        self.cartes = [Carte(couleur, hauteur) for hauteur in HAUTEURS[hauteur_min:]
                                           for couleur in COULEURS]
        if nb ==32:
            #il faut rajouter l'As
            self.cartes.extend([Carte(couleur, '1') for couleur in COULEURS])


    def battre(self):
        '''
        mélange le paquet de façon aléatoire
        '''
        random.shuffle(self.cartes)

    def couper(self):
        '''
        simule le fait de couper le paquet en deux à un endroit aléatoire
        puis de permuter les deux parties "dessus - dessous"
        '''
        zone_de_coupe=random.randint(1,self.nb_cartes)
        self.cartes=self.cartes[zone_de_coupe:]+self.cartes[:zone_de_coupe]

    def est_vide(self):
        if self.nb_cartes==0:
            return True 
        else:
            return False

    def remplir(self, cartes):
        '''
        cartes est une liste d'objets Carte
        cette méthode ajoute les cartes en question au paquet
        '''
        self.cartes.extend(cartes)

    def tirer(self):
        '''
        renvoie la carte tirée au sommet du paquet
        si le paquet est vide, lève une exception
        '''
        if self.nb_cartes==0:
            assert 'paquet vide'
        else:
            return self.cartes.pop(0)

    def getCartes(self):
        return self.cartes

def affiche_jeu(liste_cartes):
    '''
    permet d'afficher en ligne une les cartes d'une liste d'objets carte
    '''
    for i in range(len(liste_cartes)):
        print(liste_cartes[i], end=';')
    print('\n')


#tests : quand vous êtes prêt

if __name__ == '__main__':
    paq = PaquetCartes(52)
    paq.battre()
    talon=[]
    for i in range(7):
        c = paq.tirer()
        print(c, end=';')
        talon.append(c)
    affiche_jeu(talon)
    print(paq.est_vide())
    paq.remplir(talon)
    affiche_jeu(paq.getCartes())
