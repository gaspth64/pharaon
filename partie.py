import random
from cartes_paquet import Carte, PaquetCartes
from mainjoueur import MainJoueur
from tapis import Tapis
from constantes import *






## la classe principale (la plus haute) : prépare et lance la partie
class Partie:
    '''
    Modélise une partie de Pharaon
    1 joueur contre 1 IA
    Attributs
    @nb_joueurs : int valant 2 par défaut
    @nb_cartes : int valant 52 par défaut
    @nb_par_joueur : int valant 7 par défaut
    @paquet : un objet de la classe Paquet
    @tapis : un objet de la classe Tapis
    @mains : liste d'objets de type MainJoueur, représentant les joueurs
    de la Partie (et leur jeu)
    @donneur : int représentant l'indice du joueur qui va distribuer
    dans la liste des mains

    Méthodes
    @afficher() : fait afficher les mains des joueurs et le tapis
    @distribuer() : remplit les mains des joueurs avec les cartes du paquet
    @start() : prépare tout pour le début du jeu
    ...

    '''
    def __init__(self, nb_joueurs=2, nb_cartes=52, nb_par_joueur=7):

        #vérification de routine
        if nb_joueurs < 1 or nb_joueurs > 4 or \
        (nb_cartes != 32 and nb_cartes != 52) or \
         nb_par_joueur > nb_cartes // nb_joueurs:
            raise ValueError(VALUE_ERROR)



        #génération du paquet de carte pour le jeu
        self.paquet = PaquetCartes(nb_cartes)
        self.paquet.battre()
        self.tapis = Tapis()

        self.nb_joueurs = nb_joueurs
        self.donneur = 0

        self.nb_par_joueur = nb_par_joueur

        #création des mains des joueurs
        # vides au départ !
        self.mains=[]
        for lettre in POSITIONS[nb_joueurs]:
            self.mains.append[Mainjoueur([],lettre)]
           
        

    def afficher(self):
        '''
        affiche les jeux des joueurs
        et le tapis
        '''
        pass
        



    def distribuer(self):
        '''
        remplit les listes de cartes des mains pour chaque joueur
        '''
        servi = (self.donneur + 1) % self.nb_joueurs
        #servi est l'indice du joueur à qui donner une carte
        for _ in range(self.nb_par_joueur):
            for _ in range(self.nb_joueurs):
                #on distribue une carte à ce joueur
                self.mains[servi].recevoir(self.paquet.tirer())
                #au prochain tour, ce sera au joueur suivant
                servi = (servi + 1) % self.nb_joueurs





    def start(self):
        '''
        mélange le paquet, coupe, distribue les cartes
        retourne la première carte du talon qui vient sur la défausse
        affiche le tout
        puis affiche ("on démarre")
        '''

        #à vous



        print("on démarre")




#test
if __name__ == '__main__':
    test = Partie()
    test.start()











