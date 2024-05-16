from cartes_paquet import *
from copy import deepcopy

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

    def classer_hauteurs(self):
        dico={}
        for carte in self.cartes:
            dico[carte.int_hauteur]=[]
        for carte in self.cartes:
            dico[carte.int_hauteur].append(carte)
        return dico

    def classer_couleurs(self):
        dico={}
        for carte in self.cartes:
            dico[carte.couleur]=[]
        for carte in self.cartes:
            dico[carte.couleur].append(carte)
        return dico
    

    def compter_points(self):
        '''
        analyse le jeu du joueur et compte les points,
        met à jour l'attribut self.pharaon et self.pts
        '''
        t=0
        while t < 2:
            t += 1
            if t == 1:
                cartes_libres = deepcopy(self)
                #on cherche un potentiel carré ou brelan
                dico_hauteurs = cartes_libres.classer_hauteurs()
                for hauteur in dico_hauteurs:
                    #pour voir s'il y a plus de 3 cartes de la même valeur 
                    if len(dico_hauteurs[hauteur]) >= 3:
                        #si il y a une figure, on retire les cartes de la hauteur concernée
                        for carte in dico_hauteurs[hauteur]:
                            cartes_libres.rejeter(carte.id)
                            
                        
                #on cherche une potentielle suite,
                dico_couleurs = cartes_libres.classer_couleurs()
                for couleur in dico_couleurs:
                    #on créer une variable contenant la taille de la liste des cartes de la couleur
                    taille = len(dico_couleurs[couleur])
                    #pour voir s'il y a 3 cartes dans la couleur
                    if taille >= 3:
                        #on s'assure qu'elles soient triées
                        dico_couleurs[couleur].sort(key=lambda x:x.int_hauteur)
                        
                        #on parcourt les cartes de la couleur indice par indice
                        for i in range(taille):
                            #on test si l'entier de la hauteur de la carte d'après est celui d'après celui de la carte
                            if dico_couleurs[couleur][(i+1)%taille].int_hauteur == (dico_couleurs[couleur][i].int_hauteur+1)%14:
                                #si c'est le cas on vérifie celle d'après
                                if dico_couleurs[couleur][(i+2)%taille].int_hauteur == (dico_couleurs[couleur][i].int_hauteur+2)%14:
                                    #si on arrive ici, c'est que la carte d'indice i est le début d'une suite
                                    #si il y a une figure, on retire les cartes de la hauteur concernée
                                    cartes_libres.rejeter(dico_couleurs[couleur][i].id)
                                    cartes_libres.rejeter(dico_couleurs[couleur][(i+1)%taille].id)
                                    cartes_libres.rejeter(dico_couleurs[couleur][(i+2)%taille].id)

                #il faut désormais faire les comptes de ce qu'il reste dans cartes_libres
                if len(cartes_libres.cartes) == 0 or (len(cartes_libres.cartes) == 1 and cartes_libres.cartes[0].valeur <= 5):
                    self.pharaon=True

                self.pts = 0
                for c in cartes_libres.cartes:
                    self.pts += c.valeur
                    
            elif t==2:
            
                cartes_libres = deepcopy(self)        
                #on cherche une potentielle suite,
                dico_couleurs = cartes_libres.classer_couleurs()
                for couleur in dico_couleurs:
                    #on créer une variable contenant la taille de la liste des cartes de la couleur
                    taille = len(dico_couleurs[couleur])
                    #pour voir s'il y a 3 cartes dans la couleur
                    if taille >= 3:
                        #on s'assure qu'elles soient triées
                        dico_couleurs[couleur].sort(key=lambda x:x.int_hauteur)
                        
                        #on parcourt les cartes de la couleur indice par indice
                        for i in range(taille):
                            #on test si l'entier de la hauteur de la carte d'après est celui d'après celui de la carte
                            if dico_couleurs[couleur][(i+1)%taille].int_hauteur == (dico_couleurs[couleur].int_hauteur+1)%14:
                                #si c'est le cas on vérifie celle d'après
                                if dico_couleurs[couleur][(i+2)%taille].int_hauteur == (dico_couleurs[couleur].int_hauteur+2)%14:
                                    #si on arrive ici, c'est que la carte d'indice i est le début d'une suite
                                    #si il y a une figure, on retire les cartes de la hauteur concernée
                                    cartes_libres.rejeter(dico_couleurs[couleur][i].id)
                                    cartes_libres.rejeter(dico_couleurs[couleur][(i+1)%taille].id)
                                    cartes_libres.rejeter(dico_couleurs[couleur][(i+2)%taille].id)

                #on cherche un potentiel carré ou brelan
                dico_hauteurs = cartes_libres.classer_hauteurs()
                for hauteur in dico_hauteurs:
                    #pour voir s'il y a plus de 3 cartes de la même valeur 
                    if len(dico_hauteurs[hauteur]) >= 3:
                        #si il y a une figure, on retire les cartes de la hauteur concernée
                        for carte in dico_hauteurs[hauteur]:
                            cartes_libres.rejeter(carte.id)
                            
                
                #il faut désormais faire les comptes de ce qu'il reste dans cartes_libres
                if len(cartes_libres.cartes) == 0 or (len(cartes_libres.cartes) == 1 and cartes_libres.cartes[0].valeur <= 5):
                    self.pharaon=True

                pts_deuxieme_sens = 0
                for c in cartes_libres.cartes:
                    pts_deuxieme_sens += c.valeur
                
                self.pts = max(self.pts, pts_deuxieme_sens)
            
    
    def choix_input(self, carte):
        '''
        renvoie : 1 si on ramasse la carte sur la défausse
                0 si on pioche au talon
        '''
        print('Entrez pour piocher :\n- dans le paquet : 0\n- dans la défausse : 1\n')
        while True:
            action = input('Action:  ')
            if int(action) == 0 or int(action) == 1:
                return int(action)
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

    #pas de figure
    #pharon ? non
    main_2 = [Carte('s','1'),Carte('c','1'),Carte('d','6'),Carte('c','Q'), Carte('h','Q'), Carte('s','Q'),Carte('d','Q')]
    main_2 = Mainjoueur(main_2)
    main_2.compter_points()
    assert main_2.pharaon==False, 'main_2 : le programme se trompe pour pharaon'
    assert main_2.pts==8, 'main_2 : le programme compte mal les points'


    #carré de 8 et brelan de 9
    #pharon ? oui
    main_3 = [Carte('c','8'), Carte('h','8'), Carte('s','8'),Carte('d','8'), Carte('h','9'), Carte('c','9'),Carte('d','9')
    main_3 = Mainjoueur(main_3)
    main_3.compter_points()
    assert main_3.pharaon==True, 'main_3 : le programme ne signale pas le pharaon'
    assert main_3.pts==0, 'main_3 : le programme compte mal les points'


    #carré de Roi, suite en pique
    #pharaon ? oui
    main_4 = [Carte('c','K'), Carte('h','K'), Carte('s','K'),Carte('d','K'), Carte('s','6'), Carte('s',7'), Carte('s','8')]
    main_4 = Mainjoueur(main_4)
    main_4.compter_points()
    assert main_4.pharaon==True, 'main_4 : le programme ne signale pas le pharaon'
    assert main_4.pts==0, 'main_4 : le programme compte mal les points'


    #brelan de 2, suite en trèfle
    #pharaon ? oui
    main_5 = [Carte('h','2'),Carte('d','2'),Carte('s','2'),Carte('c','2'), Carte('c','3'),Carte('c','4'), Carte('d','5')]
    main_5 = Mainjoueur(main_5)
    main_5.compter_points()
    assert main_5.pharaon==True, 'main_5 : le programme ne signale pas le pharaon'
    assert main_5.pts==0, 'main_5 : le programme compte mal les points'


    #brelan de 10
    #pharaon ? non
    main_6 = [Carte('h','2'),Carte('d','2'),Carte('s','2'),Carte('c','2'), Carte('c','3'),Carte('c','4'), Carte('d','5')]
    main_6 = Mainjoueur(main_6)
    main_6.compter_points()
    assert main_6.pharaon==False, 'main_6 : le programme se trompe sur pharaon'
    assert main_6.pts==0, 'main_6 : le programme compte mal les points'


    #brelan de valets et carré de rois
    #pharaon ? oui
    main_7 = [Carte('s','J'),Carte('h','J'),Carte('c','J'),Carte('c','K'),Carte('s','K'),Carte('d','K'),Carte('h','K')]
    main_7 = Mainjoueur(main_7)
    main_7.compter_points()
    assert main_7.pharaon==True, 'main_7 : le programme ne signale pas le pharaon'
    assert main_7.pts==0, 'main_7 : le programme compte mal les points'

    #brelan de 9 et brelan de 6
    #pharaon ? oui
    main_8 = [Carte('h','9'), Carte('c','9'),Carte('d','9'), Carte('h','6'), Carte('c','6'),Carte('d','6'), Carte('d','5')]
    main_8 = Mainjoueur(main_8)
    main_8.compter_points()
    assert main_8.pharaon==True, 'main_8 : le programme ne signale pas le pharaon'
    assert main_8.pts==5, 'main_8 : le programme compte mal les points'

    #brelan de 2 et suite en pique
    #pharaon ? oui
    main_9 = [Carte('h','2'),Carte('d','2'),Carte('s','2'),Carte('c','J'), Carte('c','Q'),Carte('c','K'), Carte('d','5')]
    main_9 = Mainjoueur(main_9)
    main_9.compter_points()
    assert main_9.pharaon==True, 'main_9 : le programme ne signale pas le pharaon'
    assert main_9.pts==3, 'main_9 : le programme compte mal les points'


    #brelan de 8
    #pharaon ? non
    main_10 = [Carte('s','6'), Carte('s','7'), Carte('s','8'), Carte('d','8'), Carte('c','8'), Carte('c','2'), Carte('c','3')]
    main_10 = Mainjoueur(main_10)
    main_10.compter_points()
    assert main_10.pharaon==False, 'main_10 : le programme se trompe pour pharaon'
    assert main_10.pts==18, 'main_10 : le programme compte mal les points'

    #suite en trèfle
    #pharaon ? non
    main_11 = [Carte('c','10'), Carte('c','J'), Carte('c','Q'),Carte('s','2') , Carte('s','6'), Carte('h','9'),Carte('h','K')]
    main_11 = Mainjoueur(main_11)
    main_11.compter_points()
    assert main_11.pharaon==False, 'main_11 : le programme se trompe pour pharaon'
    assert main_11.pts==27, 'main_11 : le programme compte mal les points'

    #suite en pique et carré de 2
    #pharaon ? oui
    main_12 = [Carte('s','6'), Carte('s','7'), Carte('s','8'),Carte('h','2'),Carte('d','2'),Carte('s','2'),Carte('c','2')]
    main_12 = Mainjoueur(main_12)
    main_12.compter_points()
    assert main_12.pharaon==True, 'main_12 : le programme ne signale pas le pharaon'
    assert main_12.pts==0, 'main_12 : le programme compte mal les points'

    #suite en trèfle et brelan de 4
    #pharaon ? oui
    main_13 = [Carte('c','2'), Carte('c','3'), Carte('c','4'), Carte('h','4'), Carte('s','4'), Carte('d','4'), Carte('h','3')]
    main_13 = Mainjoueur(main_13)
    main_13.compter_points()
    assert main_13.pharaon==True, 'main_13 : le programme ne signale pas le pharaon'
    assert main_13.pts==3, 'main_13 : le programme compte mal les points'

    #suite en trèfle et brelan de Roi
    #pharaon ? non
    main_14 = [Carte('c','8'), Carte('c','9'), Carte('c','10'), Carte('c','J'), Carte('c',K), Carte('h',K), Carte('d',K)]
    main_14 = Mainjoueur(main_14)
    main_14.compter_points()
    assert main_14.pharaon==False, 'main_14 : le programme se trompe pour pharaon'
    assert main_14.pts==8, 'main_14 : le programme compte mal les points'

    #brelan de 10
    #pharaon ? non
    main_15 = [Carte('d','8'), Carte('d','9'), Carte('d','10'),Carte('c','10'),Carte('h','10'),Carte('s','2'), Carte('s','6')]
    main_15 = Mainjoueur(main_15)
    main_15.compter_points()
    assert main_15.pharaon==False, 'main_15 : le programme se trompe pour pharaon'
    assert main_15.pts==25, 'main_15 : le programme compte mal les points'

    #2 suites en coeur
    #pharaon ? oui
    main_16 = [Carte('h','2'), Carte('h','3'), Carte('h','4'), Carte('h','5'), Carte('h','6'),' Carte('h',''7'),Carte('c','3')]
    main_16 = Mainjoueur(main_16)
    main_16.compter_points()
    assert main_16.pharaon==True, 'main_16 : le programme ne signale pas le pharaon'
    assert main_16.pts==3, 'main_16 : le programme compte mal les points'



        '''
        print('- on créer un paquet que de 52 cartes')
        paq = PaquetCartes(52)
        print('- on le bat')
        paq.battre()
        main0=[]
        main2 = Mainjoueur([])
        print('- on a créer une main, est-elle vide :',main2.estvide())
        for i in range(7):
            c = paq.tirer()
            print('carte tirée du paquet : ',c,'\n')
            main0.append(c)
        main1 = Mainjoueur(main0, 'N')
        #afficher test aussi trier
        print(' MAIN 1 :')
        main1.afficher()
        main1.compter_points()
        print('Valeur de la main 1 : ',main1.pts)
        print("Y'a-t-il Pharaon ? : ", main1.pharaon)
        '''
