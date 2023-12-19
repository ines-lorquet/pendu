import pygame
import pygame_menu
import sys
import random
pygame.init()

LARGEUR, HAUTEUR = 800, 600
FOND_COULEUR = (201, 201, 201)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLANC = (255,255,255)
POLICE = pygame.font.Font("Simplify.ttf", 55)


texte_gagne = POLICE.render("Bravo, vous avez trouvé le mot secret !", True, NOIR)
texte_bienvenue = POLICE.render("Bienvenue sur le pendu", True, NOIR)
texte_rect = texte_bienvenue.get_rect(center=(500 // 2, 650 // 2))
texte_perdu = POLICE.render("Perdu", True, NOIR)
texte2_rect = texte_perdu.get_rect(center=(600 // 2, 650 // 2))
texte4_rect = texte_gagne.get_rect(center=(900 // 2, 650 // 2))
texte_perdu = POLICE.render("PERDU !   Le mot était  :", True, NOIR)
texte_gagne = POLICE.render("BRAVO !   Vous avez trouvé le mot du pendu", True, NOIR)
texte_bienvenue = POLICE.render("Bienvenue sur le pendu", True, NOIR)

mot = []
with open("mots.txt") as doc:
    for ligne in doc:
        mot.append(ligne.rstrip("\n"))

mot_a_deviner = random.choice(mot)
lettres_devinees = set()
lettres_incorrectes = set()
texte_mot=POLICE.render(mot_a_deviner, True, NOIR)
texte5_rect = texte_mot.get_rect(center=(1150 // 2, 650 // 2))

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Pendu")


def dessiner_pendu(erreurs):
        #vertical de gauche
        pygame.draw.line(fenetre, NOIR, (50,50), (50,300), 15)
        #horizontal du haut
        pygame.draw.line(fenetre, NOIR, (43,50), (200,50), 15)
        pygame.draw.line(fenetre, NOIR, (200, 44), (200,100), 5)
        pygame.draw.line(fenetre, NOIR, (90, 50), (50,90), 5)
        # horizontal du bas
        pygame.draw.line(fenetre, NOIR, (27, 300), (200,300), 18)
        if erreurs == 0:
            return
        elif erreurs == 1:
            #1 rond
            pygame.draw.ellipse(fenetre, NOIR, 
            pygame.Rect(175, 80, 50, 40)) 
        elif erreurs == 2:
            #1 rond
            pygame.draw.ellipse(fenetre, NOIR, 
            pygame.Rect(175, 80, 50, 40))    
            #2 corps
            pygame.draw.line(fenetre, NOIR, (200, 200), (200,50), 5)
        elif erreurs == 3:
            #1 rond
            pygame.draw.ellipse(fenetre, NOIR, 
            pygame.Rect(175, 80, 50, 40)) 
            #2 corps
            pygame.draw.line(fenetre, NOIR, (200, 200), (200,50), 5)
            #2 bras gauche
            pygame.draw.line(fenetre, NOIR, (170, 190), (200,140), 5)
        elif erreurs == 4:
            #1 rond 
            pygame.draw.ellipse(fenetre, NOIR, 
            pygame.Rect(175, 80, 50, 40)) 
            #2 corps
            pygame.draw.line(fenetre, NOIR, (200, 200), (200,50), 5)
            #2 bras gauche
            pygame.draw.line(fenetre, NOIR, (170, 190), (200,140), 5)
            #3 bras droit
            pygame.draw.line(fenetre, NOIR, (230, 190), (200,140), 5)
        elif erreurs == 5:
            #1 rond
            pygame.draw.ellipse(fenetre, NOIR, 
            pygame.Rect(175, 80, 50, 40)) 
            #2 corps
            pygame.draw.line(fenetre, NOIR, (200, 200), (200,50), 5)
            #2 bras gauche
            pygame.draw.line(fenetre, NOIR, (170, 190), (200,140), 5)
            #3 bras droit
            pygame.draw.line(fenetre, NOIR, (230, 190), (200,140), 5)
            #5 jambe gauche
            pygame.draw.line(fenetre, NOIR, (170,260), (200, 200), 5)
        elif erreurs == 6:
            #1 rond
            pygame.draw.ellipse(fenetre, NOIR, 
            pygame.Rect(175, 80, 50, 40)) 
            #2 corps
            pygame.draw.line(fenetre, NOIR, (200, 200), (200,50), 5)
            # bras gauche
            pygame.draw.line(fenetre, NOIR, (170, 190), (200,140), 5)
            #3 bras droit
            pygame.draw.line(fenetre, NOIR, (230, 190), (200,140), 5)
            #5 jambe gauche
            pygame.draw.line(fenetre, NOIR, (170,260), (200, 200), 5)
            #6 jambe droite
            pygame.draw.line(fenetre, NOIR, (230,260), (200, 200), 5)
                    
        elif erreurs>=7:
            #1 rond
            pygame.draw.ellipse(fenetre, NOIR, 
            pygame.Rect(175, 80, 50, 40)) 
            #2 corps
            pygame.draw.line(fenetre, NOIR, (200, 200), (200,50), 5)
            # bras gauche
            pygame.draw.line(fenetre, NOIR, (170, 190), (200,140), 5)
            #3 bras droit
            pygame.draw.line(fenetre, NOIR, (230, 190), (200,140), 5)
            #5 jambe gauche
            pygame.draw.line(fenetre, NOIR, (170,260), (200, 200), 5)
            #6 jambe droite
            pygame.draw.line(fenetre, NOIR, (230,260), (200, 200), 5)
            #croix gauche
            pygame.draw.line(fenetre, BLANC, (185,98), (195, 108), 2)
            pygame.draw.line(fenetre, BLANC, (195,98), (185, 108), 2)
            #croix droite
            pygame.draw.line(fenetre, BLANC, (205,98), (215, 108), 2)
            pygame.draw.line(fenetre, BLANC, (215,98), (205, 108), 2)
            
            fenetre.blit(texte_perdu, texte2_rect)
            fenetre.blit(texte_mot,texte5_rect) 

def inserer_mot():
    fenetre.fill(FOND_COULEUR)
    afficher_texte = POLICE.render("Insérer un mot à deviner :", True, NOIR)
    fenetre.blit(afficher_texte, (LARGEUR // 2 - afficher_texte.get_width() // 2, HAUTEUR // 2 - 50))
    pygame.display.flip()

    nouveau_mot = ""
    ajout_termine = False

    while not ajout_termine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ajout_termine = True
                elif event.key == pygame.K_BACKSPACE:
                    nouveau_mot = nouveau_mot[:-1]
                elif event.unicode.isalpha():
                    nouveau_mot += event.unicode   



        fenetre.fill(FOND_COULEUR)
        afficher_texte = POLICE.render("Insérer un mot à deviner :", True, NOIR)
        fenetre.blit(afficher_texte, (LARGEUR // 2 - afficher_texte.get_width() // 2, HAUTEUR // 2 - 50))

        afficher_nouveau_mot = POLICE.render(nouveau_mot, True, NOIR)
        text_x = LARGEUR // 2 - afficher_nouveau_mot.get_width() // 2
        text_y = LARGEUR // 2 - afficher_nouveau_mot.get_height() // 2
        fenetre.blit(afficher_nouveau_mot, (text_x, text_y))
        pygame.display.flip()
        
    maj_mot=nouveau_mot.upper()
    with open("mots.txt", 'a') as fichier:
        fichier.write(maj_mot.strip() + "\n")


def afficher_mot_masque(mot, lettres_devinees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_devinees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "_ "
    return mot_affiche.strip()


def start_the_game():
    global mot_a_deviner, lettres_devinees, lettres_incorrectes

    lettres_devinees = set()
    lettres_incorrectes = set()
    erreurs = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key >= 97 and event.key <= 122:
                    lettre = chr(event.key).upper()
                    if lettre not in lettres_devinees and lettre not in lettres_incorrectes:
                        if lettre in mot_a_deviner:
                            lettres_devinees.add(lettre)
                        else:
                            lettres_incorrectes.add(lettre)
                            erreurs += 1

        fenetre.fill(FOND_COULEUR)

        mot_masque = afficher_mot_masque(mot_a_deviner, lettres_devinees)
        mot_affiche = POLICE.render(mot_masque, True, NOIR)
        fenetre.blit(mot_affiche, (300, 400))

        lettres_incorrectes_affiche = ", ".join(sorted(lettres_incorrectes))
        lettres_incorrectes_surface = POLICE.render(f"Lettres  incorrectes  :  {lettres_incorrectes_affiche}", True, ROUGE)
        fenetre.blit(lettres_incorrectes_surface, (300, 500))

        dessiner_pendu(erreurs)

        if set(mot_a_deviner) == lettres_devinees:
            fenetre.blit(texte_gagne, texte4_rect)


        pygame.display.flip()


menu = pygame_menu.Menu('PENDU', 800, 600, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('JOUER', start_the_game)
menu.add.button('INSERER',inserer_mot)
menu.add.button('QUITTER', pygame_menu.events.EXIT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fenetre.fill(FOND_COULEUR)
    fenetre.blit(texte_bienvenue, texte_rect)

    menu.mainloop(fenetre)
    pygame.display.flip()
