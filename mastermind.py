#=============================================================
# MODULE
#=============================================================
import pygame
pygame.init()

from random import randint

#=============================================================
#FONCTION
#=============================================================

#=============================================================
#graphique
#=============================================================
def afficher_grille():
    """affiche la grille vide"""
    #grille
    for i in range (1,11):
        pygame.draw.line(surface = surface_jeu , color = N , start_pos = (0,i*taille_case_y), end_pos = (taille_fenetre_x,i*taille_case_y), width = largeur_trait) 
    for i in range (1,7) :
        pygame.draw.line(surface = surface_jeu , color = N , start_pos = (i*taille_case_x,0), end_pos = (i*taille_case_x,taille_fenetre_y) , width = largeur_trait) 
    #en-tête
    for i in range (1,11):
        texte_numero = calibri_petit.render("coup n°"+str(i) ,True,N)
        surface_jeu.blit(texte_numero,(0,(taille_fenetre_y-(i*taille_case_y)+taille_case_y/2)))
    #donnée autre que coup n°...
    texte_resultat = calibri_petit.render("Résultat" ,True,N)
    surface_jeu.blit(texte_resultat,(0,(taille_fenetre_y-(11*taille_case_y)+taille_case_y/2)))
    texte_P = calibri_petit.render("P" ,True,N)
    surface_jeu.blit(texte_P,((6*taille_case_x)+taille_case_x/2,25))
    texte_MP = calibri_petit.render("MP" ,True,N)
    surface_jeu.blit(texte_MP,((5*taille_case_x)+taille_fenetre_x/21,25))
    
def afficher_recap():
    """fonction qui taduit la liste des choix déja fait en info pour remplir la grille"""
    for num_ligne in range (len(recap)):
        ligne=recap[num_ligne]
        for num_colonne in range (len(ligne['liste'])):
            colonne=ligne['liste'][num_colonne]
            # on choisit les couleurs
            if colonne == "V" :
                couleur = V
            elif colonne == "R" :
                couleur = R
            elif colonne == "B" :
                couleur = B
            elif colonne == "N" :
                couleur = N
            elif colonne == "G" :
                couleur = G
            elif colonne == "J" :
                couleur = J
            else :
                print("erreur couleur non referencer dans la foncion afficher resultat")
            # on positionne tt ca
            pygame.draw.circle(surface = surface_jeu, color = couleur , center = (int(taille_case_x*(num_colonne+1.5)),int(taille_case_y*(10.5-num_ligne))) , radius = taille_rond , width = taille_rond)
        
            #on entre le nombre de parfait et de mal placé
            texte_nombre_de_mal_place = calibri_petit.render(str(ligne['mal placé']) ,True,N)
            surface_jeu.blit(texte_nombre_de_mal_place,((int(5.5*taille_case_x)),(int(taille_fenetre_y-(0.5+num_ligne)*taille_case_y))))
            
            texte_nombre_de_parfait = calibri_petit.render(str(ligne['parfait']) ,True,N)
            surface_jeu.blit(texte_nombre_de_parfait,((int(6.5*taille_case_x)),(int(taille_fenetre_y-(0.5+num_ligne)*taille_case_y))))

def afficher_proposition_actuelle():
    for num_colonne in range (len(proposition_actuelle)):
        colonne=proposition_actuelle[num_colonne]
        # on choisit les couleurs
        if colonne == "V" :
            couleur = V
        elif colonne == "R" :
            couleur = R
        elif colonne == "B" :
            couleur = B
        elif colonne == "N" :
            couleur = N
        elif colonne == "G" :
            couleur = G
        elif colonne == "J" :
            couleur = J
        else :
            couleur = blanc
        pygame.draw.circle(surface = surface_jeu, color = couleur , center = (int(taille_case_x*(num_colonne+1.5)),int(taille_case_y*(position[1]+0.5))) , radius = taille_rond , width = taille_rond)

def afficher_liste_de_depart():
    """affiche la liste de depart sous forme graphique"""
    for i in range (len(liste_de_depart)):
        element=liste_de_depart[i]
        # on choisit les couleurs
        if element == "V" :
            couleur = V
        elif element == "R" :
            couleur = R
        elif element == "B" :
            couleur = B
        elif element == "N" :
            couleur = N
        elif element == "G" :
            couleur = G
        elif element == "J" :
            couleur = J
        pygame.draw.circle(surface = surface_jeu, color = couleur , center = (int(taille_case_x*(i+1.5)),int(taille_case_y*0.5)) , radius = taille_rond , width = taille_rond)
    
def marquer_case_active():
    """fonction qui fait apparaitre un carée orange autour de la case active"""
    pygame.draw.line(surface = surface_jeu , color = orange , start_pos = (position[0]*taille_case_x , position[1]*taille_case_y), end_pos = (position[0]*taille_case_x,(position[1]+1)*taille_case_y), width = largeur_trait)
    pygame.draw.line(surface = surface_jeu , color = orange , start_pos = (position[0]*taille_case_x , position[1]*taille_case_y), end_pos = ((position[0]+1)*taille_case_x,position[1]*taille_case_y), width = largeur_trait)
    pygame.draw.line(surface = surface_jeu , color = orange , start_pos = ((position[0]+1)*taille_case_x , (position[1]+1)*taille_case_y), end_pos = (position[0]*taille_case_x,(position[1]+1)*taille_case_y), width = largeur_trait)
    pygame.draw.line(surface = surface_jeu , color = orange , start_pos = ((position[0]+1)*taille_case_x , (position[1]+1)*taille_case_y), end_pos = ((position[0]+1)*taille_case_x,position[1]*taille_case_y), width = largeur_trait)

#=============================================================
#fenetre de fin
#=============================================================

def victoire():
    texte_victoire1 = calibri_grand.render("Victoire en ",True,cyan)
    texte_victoire2 = calibri_grand.render(str(len(recap)) + " coups" ,True,cyan)
    run = True
    while run : # on a pas demander a fermer le programme
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # on demande a fermer le programme
                return "fermer"
                
            if event.type == pygame.KEYDOWN :
                #======================================
                # si on clique sur espace on recommence
                #======================================
                if event.key == pygame.K_SPACE :
                    return "recommencer"
                
        surface_jeu.fill(blanc)# on initialise
        afficher_recap()
        afficher_grille()
        surface_jeu.blit(texte_victoire1,(taille_fenetre_x/20,(4*taille_fenetre_y/10)))
        surface_jeu.blit(texte_victoire2,(taille_fenetre_x/6,(5*taille_fenetre_y/10)))
        afficher_liste_de_depart()
        pygame.display.flip()

def defaite():
    texte_defaite1 = calibri_grand.render("Défaite",True,cyan)
    run = True
    while run : # on a pas demander a fermer le programme
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # on demande a fermer le programme
                return "fermer"
                
            if event.type == pygame.KEYDOWN :
                #======================================
                # si on clique sur espace on recommence
                #======================================
                if event.key == pygame.K_SPACE :
                    return "recommencer"
                
        surface_jeu.fill(blanc)# on initialise
        afficher_recap()
        afficher_grille()
        surface_jeu.blit(texte_defaite1,(taille_fenetre_x/5,(4*taille_fenetre_y/10)))
        afficher_liste_de_depart()
        pygame.display.flip()

#=============================================================
#lié au jeu
#=============================================================

def choisir_liste_de_depart():
    """fonction qui choisit une liste aleatoire de 4 couleur"""
    return [liste_des_couleurs[randint(0,5)]]+[liste_des_couleurs[randint(0,5)]]+[liste_des_couleurs[randint(0,5)]]+[liste_des_couleurs[randint(0,5)]]

def valider_saisie() :
    """fonction qui renvoie True si la saisie contenue dans proposition_actuelle est valide False sinon"""
    résultat = True
    for element in proposition_actuelle :
        if element not in liste_des_couleurs :
            résultat = False
    return résultat

def tester_le_choix_de_l_utilisateur():
    """renvoit le nombre de jeton bien placé par l utilisateur"""
    # on compte le nb de parfaitement placer
    liste_des_parfaits = []
    for i in range (4) :
        if proposition_actuelle[i] == liste_de_depart[i] :
            liste_des_parfaits += [i]
    nombre_de_parfait = len(liste_des_parfaits)
            
    #on compte le nb de bonne couleur mal placé
    proposition_actuelle_sans_parfait = [proposition_actuelle[i] for i in range (len(proposition_actuelle)) if i not in liste_des_parfaits]
    liste_de_depart_sans_parfait = [liste_de_depart[i] for i in range (len(liste_de_depart)) if i not in liste_des_parfaits]
    nombre_de_mal_place = 0
    
    for i in range (len(proposition_actuelle_sans_parfait)) :
        if proposition_actuelle_sans_parfait[i] in liste_de_depart_sans_parfait :
            liste_de_depart_sans_parfait.remove(proposition_actuelle_sans_parfait[i])
            nombre_de_mal_place += 1
    
    return nombre_de_parfait , nombre_de_mal_place

def position_souris() :
    """renvoit un tuple correspondant aux coordonée sur le plateau de la souris """
    position = pygame.mouse.get_pos()
    x = position[0]//taille_case_x
    y = position[1]//taille_case_y
    return (x,y)



#=============================================================
# CONSTANTE
#=============================================================

#=============================================================
#lié aux graphismes
#=============================================================
# couleur
# B = bleu
B = (0,0,175)
# J = jaune
J = (242,242,0)
# R = rouge
R = (220,0,0)
# N = noir
N = (0,0,0)
# V = vert
V = (0,175,0)
# G = gris
G = (175,175,175)
cyan = (0,175,255)
blanc = (255,255,255)
orange = (255,123,0)

# taille
taille_fenetre_x = 400
taille_fenetre_y = 607
taille_case_x = int(taille_fenetre_x/7)
taille_case_y = int(taille_fenetre_y/11)
largeur_trait = 3
taille_rond = int(taille_fenetre_y/30)
#police
calibri_petit = pygame.font.SysFont(name = "calibri", size = int(taille_fenetre_x/30), bold=False, italic=False)
calibri_moyen = pygame.font.SysFont(name = "calibri", size = int(taille_fenetre_x/21), bold=False, italic=False)
calibri_moyen_grand = pygame.font.SysFont(name = "calibri", size = int(taille_fenetre_x/6), bold=True, italic=False)
calibri_grand = pygame.font.SysFont(name = "calibri", size = int(taille_fenetre_x/5), bold=True, italic=False) 
#=============================================================
#lié au jeu
#=============================================================
recap = []
liste_des_couleurs = ["B","J","R","N","V","G"]
liste_de_depart = choisir_liste_de_depart()
position = (1,10)
proposition_actuelle = ["NC"]*4
#=============================================================
#lié aux fenetres
#=============================================================
run = True
runintro = True
surface_jeu = pygame.display.set_mode((taille_fenetre_x , taille_fenetre_y))

#=============================================================
#PROGRAMME
#=============================================================

#=============================================================
#INTRO
#=============================================================
texte_intro1 = calibri_moyen_grand.render("MASTERMIND",True,cyan)
texte_intro2 = calibri_moyen.render("Ce jeu se joue seul contre l'ordinateur.",True,cyan)
texte_intro3 = calibri_moyen.render("Le but du jeu est de trouver la combinaison de",True,cyan)
texte_intro4 = calibri_moyen.render("4 couleurs parmi les couleurs suivantes :",True,cyan)
texte_intro5 = calibri_moyen.render("Bleu",True,B)
texte_intro6 = calibri_moyen.render("Gris",True,G)
texte_intro7 = calibri_moyen.render("Jaune",True,J)
texte_intro8 = calibri_moyen.render("Noir",True,N)
texte_intro9 = calibri_moyen.render("Rouge",True,R)
texte_intro10 = calibri_moyen.render("Vert",True,V)
texte_intro11 = calibri_moyen.render("Pour entrer une couleur appuyer sur la touche ",True,cyan)
texte_intro12 = calibri_moyen.render("du clavier corespondant a son initiale lorsque la ",True,cyan)
texte_intro13 = calibri_moyen.render("case est selectionner,",True,cyan)
texte_intro14 = calibri_moyen.render("Pour selectionner une case cliquer dessus. ",True,cyan)
texte_intro15 = calibri_moyen.render("appuyer sur entrée pour valider la ligne actuelle",True,cyan)
texte_intro16 = calibri_moyen.render("dans la colonne P vous verrez le nombre de",True,cyan)
texte_intro17 = calibri_moyen.render("couleurs parfaitements placées et dans la colonne",True,cyan)
texte_intro18 = calibri_moyen.render("MP le nombre de bonnes couleurs mal placée",True,cyan)
texte_intro19 = calibri_moyen.render("Appuyer sur espace pour recommencer.",True,cyan)
texte_intro20 = calibri_moyen.render("Appuyer sur une touche pour continuer.",True,cyan)
while runintro : # on a pas demander a fermer le programme
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # on demande a fermer le programme
            runintro = False
            run = False  
        if event.type == pygame.KEYDOWN :# si une touche est cliqué on verifie qu'elle est repertorié
            runintro = False            
    surface_jeu.fill(blanc)# on initialise
    surface_jeu.blit(texte_intro1,(0,(taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro2,(10,(3*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro3,(10,(4*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro4,(10,(5*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro5,(20,(6*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro6,(20,(7*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro7,(20,(8*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro8,(20,(9*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro9,(20,(10*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro10,(20,(11*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro11,(10,(12*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro12,(10,(13*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro13,(10,(14*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro14,(10,(15*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro15,(10,(16*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro16,(10,(17*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro17,(10,(18*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro18,(10,(19*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro19,(10,(20*taille_fenetre_y/22)))
    surface_jeu.blit(texte_intro20,(10,(21*taille_fenetre_y/22)))
    pygame.display.flip()
        
#=============================================================
#JEU
#=============================================================
while run : # on a pas demander a fermer le programme
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # on demande a fermer le programme
            run = False
            
        if event.type == pygame.KEYDOWN :# si une touche est cliqué on verifie qu'elle est repertorié
            #=============================================================
            # si on clique sur une lettre a laquelle corespond une couleur
            #=============================================================
            if event.key == pygame.K_b :
                couleur = "B"
            elif event.key == pygame.K_r :
                couleur = "R"
            elif event.key == pygame.K_g :
                couleur = "G"
            elif event.key == pygame.K_v :
                couleur = "V"
            elif event.key == pygame.K_n :
                couleur = "N"
            elif event.key == pygame.K_j :
                couleur = "J"
            else :
                couleur = "inconnue"
            if couleur != "inconnue" :# si la couleur est valide
                proposition_actuelle[position[0]-1] = couleur # on actualise la couleur
                if position[0] != 4 : # on avance d'une case
                    position = ((position[0]+1),position[1])
                else : # si on depasse on revient au déut
                    position = (1,position[1])
            
            #========================
            # si on clique sur entrée
            #========================
            if event.key == pygame.K_RETURN :
                if valider_saisie() :# si a saisie est valide
                    nombre_de_parfait , nombre_de_mal_place = tester_le_choix_de_l_utilisateur()
                    recap += [{"liste" : tuple(proposition_actuelle) , "parfait" : nombre_de_parfait , "mal placé" : nombre_de_mal_place}]
                    if nombre_de_parfait == 4:# si on gagne
                        choix_utilisateur = victoire()
                        if choix_utilisateur == "recommencer" :
                            recap = []
                            liste_de_depart = choisir_liste_de_depart()
                            position = (1,10)
                            proposition_actuelle = ["NC"]*4
                        elif choix_utilisateur == "fermer":
                            run = False
                    elif len(recap)>9:# si il y a défaite
                        choix_utilisateur = defaite()
                        if choix_utilisateur == "recommencer" :
                            recap = []
                            liste_de_depart = choisir_liste_de_depart()
                            position = (1,10)
                            proposition_actuelle = ["NC"]*4
                        elif choix_utilisateur == "fermer":
                            run = False
                    else :
                        position = (1,position[1]-1)
                        proposition_actuelle = ["NC"]*4
                    
            
            #======================================
            # si on clique sur espace on recommence
            #======================================
            if event.key == pygame.K_SPACE :
                recap = []
                liste_de_depart = choisir_liste_de_depart()
                position = (1,10)
                proposition_actuelle = ["NC"]*4
                    
    if pygame.mouse.get_pressed() == (1,0,0) : #si on clique
        if position_souris()[1] == 10-len(recap) and 0<position_souris()[0]<5 :#on verifie que la position est corecte
            position = position_souris() #on modifie la case active
            
    surface_jeu.fill(blanc)# on initialise
    afficher_recap()
    afficher_grille()
    afficher_proposition_actuelle()
    marquer_case_active()
    pygame.display.flip()
pygame.quit()# on ferme la fenetre