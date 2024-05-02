from cartes_paquet import *

class Mainjoueur:

    def __init__(self, cartes, position='S'):
        self.cartes=cartes
        self.position=position
        #jalon 3
        self.pts = 0
        self.figure = 0
        self.pharaon = False


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

    def classer_hauteurs(self, lst):
        dico={}
        for carte in lst:
            dico[carte.int_hauteur]=[]
        for carte in lst:
            dico[carte.int_hauteur].append(carte)
        return dico

    def classer_couleurs(self, lst):
        dico={}
        for carte in lst:
            dico[carte.couleur]=[]
        for carte in lst:
            dico[carte.couleur].append(carte)
        return dico
    
    def detecter_carre_brelan(self, cartes_libres):
        '''
        analyse une liste de cartes
        renvoie une liste des cartes ne formant ni un carré, ni un brelan
        et met à jour self.pts en retirant les points des cartes formant une des 2 figure
        '''
        trie_hauteur = cartes_libres.classer_hauteurs()
        self.figure -= 1
        #on parcourt valeur par valeur
        for hauteur in trie_hauteur:
            #pour voir s'il y a plus de 3 cartes de la même valeur 
            if len(trie_hauteur[hauteur]) >= 3:
                #on signale la figure à l'attribut concerné de l'instance
                self.figure += 1
                #on retire leurs valeurs si on trouve une figure
                self.pts -= (hauteur*len(trie_hauteur[hauteur]))
                #on tetire les cartes des cartes libres
                cartes_libres.remove(c for c in trie_hauteur[hauteur])
        #on renvoie les cartes encore aptes à former une suite
        return cartes_libres

    def detecter_suite(self, cartes_libres):
        '''
        analyse la main
        renvoie une liste des cartes ne formant pas une suite
        et met à jour self.pts en retirant les points des cartes formant cette figure
        '''
        trie_couleur = self.classer_couleurs()
        self.figure -= 1
        #on parcourt couleur par couleur
        for couleur in trie_couleur:
            #pour voir s'il y a 3 cartes dans la couleur
            if len(trie_couleur[couleur]) >= 3:
                #on créer une liste vide pour les valeurs des hauteurs
                hauteurs_nbr = []
                #on ajoute le nombre de la hauteur 
                for carte in trie_couleur[couleur]:
                    hauteurs_nbr.append(carte.int_hauteur)
                #on vérifie s'il y une suite
                for i in range(len(hauteurs_nbr)):
                    if (hauteurs_nbr[i]+1)%13 == hauteurs_nbr[(i+1)%len(hauteurs_nbr)]:
                        if (hauteurs_nbr[i]+2)%13 == hauteurs_nbr[(i+2)%len(hauteurs_nbr)]:
                            #on signale la figure à l'attribut concerné de l'instance
                            self.figure += 1
                            suite = [hauteurs_nbr[i],hauteurs_nbr[i+1%len(hauteurs_nbr)],hauteurs_nbr[i+2%len(hauteurs_nbr)]]
                            #on retire leurs valeurs si on trouve une figure
                            self.pts -= sum(c.valeur() for c in suite)
                            #on retire les cartes  des cartes libres
                            cartes_libres.remove(c for c in suite)
        #on renvoie les cartes formant un carré ou un brelan
        return cartes_libres

    def compter_points(self):
        '''
        analyse le jeu du joueur et compte les points,
        met à jour l'attribut self.pharaon et self.pts
        '''
        #on compte d'abord les points de toutes les cartes
        self.pts = 0
        for carte in self.cartes:
            self.pts += carte.valeur
        
        #on cherche les figures en procédant dans deux sens différents
        if len(self.detecter_carre_brelan(self.detecter_suite(self.cartes))) <= 1 \
                and self.pts <= 5:
            self.pharaon = True
        elif len(self.detecter_suite(self.detecter_carre_brelan(self.cartes))) <= 1 \
                and self.pts <= 5:
            self.pharaon = True
    
    def choix_input(self, carte):
        '''
        renvoie : 1 si on ramasse la carte sur la défausse
                0 si on pioche au talon
        '''
        print('Entrez pour piocher :\n- dans le paquet : 0\n- dans la défausse : 1\n')
        while True:
            action = int(input('Action:  '))
            if action == 0 or action == 1:
                return action
            else:
                print("L'action n'est pas valide.RTFM")




    def choix_output(self):
        '''
        renvoie l'id de la carte a rejeter
        si pharaon, renvoie False
        '''
        #on met à jour self.pts et self.pharaon
        self.compter_points()

        while True:
            carte_jetee_provi = input("Entrez l'id de la carte a jeter, exemple = sK ou c3:  ")
            carte_jetee=''
            for i in range(len(carte_jetee_provi)):
                if carte_jetee_provi[i] in DICO_VERIF.keys():
                    carte_jetee= carte_jetee+DICO_VERIF[carte_jetee_provi[i]]

            for i in range(len(self.cartes)):
                if self.cartes[i].id==carte_jetee:
                    return carte_jetee
            print("saisie pas valide.RTFM")

        


# jalon 2bis =>

class MainjoueurIA(Mainjoueur):

    def __init__(self, cartes, position='N'):
        #on appelle le constructeur de la classe parente
        Mainjoueur.__init__(self, cartes, position)
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


    def score(self, carte):
        pass


if __name__=='__main__':
    print('on créer un paquet que de 52 cartes')
    paq = PaquetCartes(52)
    print('on le bat')
    paq.battre()
    main0=[]
    main2 = Mainjoueur([])
    print('on a créer une main, est-elle vide :',main2.estvide())
    for i in range(12):
        c = paq.tirer()
        print(c, end=';')
        main0.append(c)
    print('\n')
    main1 = Mainjoueur(main0, 'N')
    #afficher test aussi trier
    main1.afficher()
    print(main1.compter_points())
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    for n in range(6):
        c = main0[n].id
        main2.recevoir(main1.rejeter(c))
    main1.afficher()
    main2.afficher()
    print(main2.estvide())
    print('main1 classée par couleurs : ',main1.classer_couleurs())
    print('main2 classée par hauteurs',main2.classer_hauteurs())