from cartes_paquet import *

class Mainjoueur:

    def __init__(self, cartes, position='S'):


        self.cartes=cartes
        self.position=position

    def estvide(self):
        return len(self.cartes)==0

    def trier(self):
        if not self.estvide():
            self.cartes.sort(key=lambda x:x.int_hauteur)

    def afficher(self):
        self.trier()
        for carte in self.cartes:
            print(carte, end=';')
        print('\n')

    def recevoir(self, carte):
        self.cartes.append(carte)

    def rejeter(self, id_carte):
        for i in range(len(self.cartes)):
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


# jalon 2bis =>

class MainJoueurIA(MainJoueur):

    def __init__(self, cartes, position='N'):
        #on appelle le constructeur de la classe parente
        MainJoueur.__init__(self, cartes, position)
        #ici c'est tout : pas d'attribut spécifique

    def choix_output(self):
        '''
        renvoie l'id de la carte choisie pour rejeter
        (après avoir vérifié qu'elle existe dans la main de l'IA)
        '''
        #jalon_2bis : la carte à rejeter est choisie de manière aléatoire
        
        return random.choice(self.cartes).id

    def choix_input(self, carte):
        '''
        renvoie : 1 si on ramasse la carte sur la défausse
                  0 si on pioche au talon
        '''
        #jalon_2bis : tirage au sort
        return random.randint(0,1)

    def compter_points(self):
        pass

    def score(self, carte):
        pass


if __name__=='__main__':
    
    paq = PaquetCartes(52)
    paq.battre()
    main0=[]
    main2 = Mainjoueur([])
    print(main2.estvide())
    for i in range(12):
        c = paq.tirer()
        print(c, end=';')
        main0.append(c)
    print('\n')
    main1 = Mainjoueur(main0, 'N')
    #afficher test aussi trier
    main1.afficher()
    for n in range(6):
        c = main0[n].id
        main2.recevoir(main1.rejeter(c))
    main1.afficher()
    main2.afficher()
    print(main2.estvide())
    print('main1 classée par couleurs : ',main1.classer_couleurs())
    print('main2 classée par hauteurs',main2.classer_hauteurs())
