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
                    # if taille >= 3:
                    #     #on s'assure qu'elles soient triées
                    #     dico_couleurs[couleur].sort(key=lambda x:x.int_hauteur)
                    #     
                    #     #on parcourt les cartes de la couleur indice par indice
                    #     for i in range(taille):
                    #         #on test si l'entier de la hauteur de la carte d'après est celui d'après celui de la carte
                    #         if dico_couleurs[couleur][(i+1)%taille].int_hauteur == (dico_couleurs[couleur].int_hauteur+1)%14:
                    #             #si c'est le cas on vérifie celle d'après
                    #             if dico_couleurs[couleur][(i+2)%taille].int_hauteur == (dico_couleurs[couleur].int_hauteur+2)%14:
                    #                 #si on arrive ici, c'est que la carte d'indice i est le début d'une suite
                    #                 #si il y a une figure, on retire les cartes de la hauteur concernée
                    #                 cartes_libres.rejeter(dico_couleurs[couleur][i].id)
                    #                 cartes_libres.rejeter(dico_couleurs[couleur][(i+1)%taille].id)
                    #                 cartes_libres.rejeter(dico_couleurs[couleur][(i+2)%taille].id)

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
            
    
    def choix_input(self, carte ,defausse):
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
        id_min=""
        sc_min=10000000
        for carte in self.cartes:
            sc=0
            for carte_extra in self.cartes:
                if carte.id==carte_extra.id:
                   sc+=0
                else:
                    if carte.int_hauteur == carte_extra.int_hauteur:
                        sc+=2
                    if (carte_extra.int_hauteur+1%13 == carte.int_hauteur and carte_extra.couleur == carte.couleur) or \
                    (carte_extra.int_hauteur-1%13 == carte.int_hauteur and carte_extra.couleur == carte.couleur):
                        sc+=2
                    if (carte_extra.int_hauteur+2%13 == carte.int_hauteur and carte_extra.couleur == carte.couleur) or \
                    (carte_extra.int_hauteur-2%13 == carte.int_hauteur and carte_extra.couleur == carte.couleur):
                        sc+=1
            print(sc)
            if sc<sc_min:
                id_min=carte.id
                sc_min=sc
        return id_min

    def choix_input(self, carte ,defausse):
        '''
        renvoie : 1 si on ramasse la carte sur la défausse
                  0 si on pioche au talon
        '''
        if self.score(carte,defausse)>0.15:
            return 1
        else:
            return 0


    def score(self, carte, defausse):
        '''
        Calcule le score d'une carte. Float 
        '''
        #on initialise le score
        sc=0
        #balaye la defausse sauf la derniere pour le score
        long=len(defausse)
        if long>1:
            
            for carte_def in defausse:  
                if carte_def.int_hauteur == carte.int_hauteur or \
                (carte_def.int_hauteur+1%13 == carte.int_hauteur and carte_def.couleur == carte.couleur) or \
                (carte_def.int_hauteur-1%13 == carte.int_hauteur and carte_def.couleur == carte.couleur):
                    sc-=0.10
              
        #balaye le main pour le score
        for carte_m in self.cartes:
            if carte_m.int_hauteur == carte.int_hauteur or \
            (carte_m.int_hauteur+1%13 == carte.int_hauteur and carte_m.couleur == carte.couleur) or \
            (carte_m.int_hauteur-1%13 == carte.int_hauteur and carte_m.couleur == carte.couleur):
                sc+=0.25
                
            if (carte_m.int_hauteur+2%13 == carte.int_hauteur and carte_m.couleur == carte.couleur) or \
            (carte_m.int_hauteur-2%13 == carte.int_hauteur and carte_m.couleur == carte.couleur):
                sc+=0.10
        return sc
            
                
# if __name__=='__main__':
# 
#     #un carré de 2 et 1 suite de carreaux : Pharaon 0
#     main_1 = [Carte('c',2),Carte('d',2),Carte('h',2),Carte('s',2),Carte('d',8), Carte('d',9), Carte('d',10)]
#     main_1 = Mainjoueur(main_1)
#     main_1.compter_points()
#     assert main_1.pharaon==True, 'la pharaon de la main 1 est reconnu par le programme'
#     assert main_1.pts==0, 'et il compte bien les points'



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

