class Node:
    """Classe représentant un noeud de l'arbre de décision"""
    def __init__(self, question: str, c1=None, c2=None):
        self.question = question
        self.c1 = c1
        self.c2 = c2

    def setChoice(self, choice, question):
        """Méthode permettant de définir les choix possibles"""
        if choice == 1:
            self.c1 = question # question est un Node
        else:
            self.c2 = question # question est un Node
#EN COURS DE DEVELOPPEMENT
take_none = Node("Le jeu est pas fini", None, None)

# Histoire si choix = 1

take_mer_poisson = Node(
    "Vous allez vers la mer et vous trouvez des poissons. Vous décidez de les mettre dans votre inventaire. Mais sur le chemin de votre exploration vous trouvez une carte de l'ile. Que faites-vous ? [1] Vous allez sur le point le plus haut de l'ile pour marquer un message d'alerte. [2] Vous prenez la carte et vous continuez votre exploration. "
)
construire_abri_choice = Node("Vous prenez le matériel et vous vous mettez à construire votre abri de survie. Il vous prend plusieurs heures, mais vous êtes enfin installé et en sécurité. Vous décidez alors d'explorer les alentours pour trouver des ressources. Où allez-vous ? [1] Vous allez vers la mer pour trouver des poissons. [2] Vous allez vers la forêt pour explorer l'ile mais vous oubliez votre sac. "
)
construire_abri_choice.setChoice(1, take_mer_poisson)
construire_abri_choice.setChoice(2, take_none)

recherche_choice= Node(
    "Vous partez à la recherche de ressources. Après avoir marché un moment, vous tombez sur un cours d'eau et décidez de vous installer pour la nuit. La nuit se passe sans encombre et le lendemain, vous reprenez votre exploration. En chemin, vous trouvez une baie remplie de coquillages et décidez de vous arrêter pour en récolter. Que faites-vous ? [1] Vous prenez les coquillages [2] Vous êtes attirer par un bruit et vous vous éloignez du cours d'eau pour voir ce qui se passe."
)
recherche_choice.setChoice(1, take_none)
recherche_choice.setChoice(2, take_none)

left_choice = Node(
    "Vous avez trouvé un couteau, un stylo et une trousse de secours autour du pilote. Que faites-vous ? [1] Vous prenez le couteau et la trousse de secours. [2] Vous ne prenez rien car cela ne vous intéresse pas."
)
left_choice.setChoice(1, recherche_choice)
left_choice.setChoice(2, take_none)

# Histoire si choix = 2

take_take_foret = Node(
    "Vous allez vers la forêt et vous trouvez des fruits. Vous décidez de les mettre dans votre inventaire. Mais sur le chemin vous tombez sur un ours, mais comme vous avez oublié votre sac vous mourrez GAME OVER. "
    )
right_choice = Node(
    "Vous prenez le colis sur la plage et vous trouvez du matériel pour faire un abri de survie. Que faites-vous ? [1] Vous prenez le matériel pour faire un abri de survie. [2] Vous ne prenez rien car cela ne vous intéresse pas."
)
right_choice.setChoice(1, construire_abri_choice)
right_choice.setChoice(2, take_none)



root = Node(
    
    "Vous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. Que faites-vous ? [1] Fouiller le corps du pilote pour récupérer des objets [2] Fouiller les colis sur la plage pour récupérer des objets"
)
root.setChoice(1, left_choice) 
root.setChoice(2, right_choice)

current: Node = root


        

import pygame as pg

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialisation de pygame
pg.init()

# Création de la fenêtre
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Jeu aventure")

# Création de la police de caractères
font = pg.font.Font(None, 30)

# Création des boutons
button_width = 200
button_height = 50
button_margin = 10
button_x = (WINDOW_WIDTH - button_width) / 2 # On centre le bouton
button_y = (WINDOW_HEIGHT - (2 * button_height + button_margin)) - 50 # On place le bouton en bas de la fenêtre

# Bouton gauche
button_left = pg.Rect(button_x, button_y, button_width, button_height) # Création du rectangle
text_left = font.render("Choix 1", True, WHITE) 
text_rect_left = text_left.get_rect(center=button_left.center) # Création du rectangle englobant

# Bouton droit
button_right = pg.Rect(button_x, button_y + button_height + button_margin, button_width, button_height) # Création du rectangle
text_right = font.render("Choix 2", True, WHITE)
text_rect_right = text_right.get_rect(center=button_right.center) # Création du rectangle englobant

# Bouton pour démarrer le jeu
button_start = pg.Rect(button_x, button_y, button_width, button_height)
text_start = font.render("Commencer le jeu", True, WHITE)
text_rect_start = text_start.get_rect(center=button_start.center)

# Bouton pour quitter le jeu
button_quit = pg.Rect(button_x, button_y + button_height + button_margin, button_width, button_height)
text_quit = font.render("Quitter le jeu", True, WHITE)
text_rect_quit = text_quit.get_rect(center=button_quit.center)

# Variable pour stocker le choix de l'utilisateur
menu_choice = None

# Boucle d'événements pour le menu
while menu_choice is None:
    for event in pg.event.get():
        # Gestion de la fermeture de la fenêtre
        if event.type == pg.QUIT:
            menu_choice = "quit"

        # Gestion des clics de souris
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Si le bouton pour démarrer le jeu est cliqué
            if button_start.collidepoint(mouse_pos):
                menu_choice = "start"

            # Si le bouton pour quitter le jeu est cliqué
            elif button_quit.collidepoint(mouse_pos):
                menu_choice = "quit"

    # Couleur de fond de la fenêtre
    window.fill(GRAY)

    # Affichage des boutons
    pg.draw.rect(window, DARK_GRAY, button_start)
    window.blit(text_start, text_rect_start)

    pg.draw.rect(window, DARK_GRAY, button_quit)
    window.blit(text_quit, text_rect_quit)

    # Mise à jour de la fenêtre
    pg.display.flip()

# Si l'utilisateur a choisi de quitter le jeu dans le menu, on sort du programme
if menu_choice == "quit":
    pg.quit()
    exit()
# Boucle d'événements
running = True
while running:
    for event in pg.event.get():
        # Gestion de la fermeture de la fenêtre
        if event.type == pg.QUIT:
            running = False

        # Gestion des clics de souris
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Si le bouton gauche est cliqué
            if button_left.collidepoint(mouse_pos):#
                current = current.c1
                print(current.question)

            # Si le bouton droit est cliqué
            elif button_right.collidepoint(mouse_pos):
                current = current.c2
                print(current.question)

    # Couleur de fond de la fenêtre
    window.fill(GRAY)

    #methode permettant de couper la question en plusieurs lignes
    def wrap_text(text, font, max_width):
        lines = []
        if font.size(text)[0] <= max_width: # Si le texte tient sur une ligne
            lines.append(text) # On ajoute la ligne
        else:
            words = text.split(' ') # On découpe le texte en mots
            i = 0 # Compteur de mots
            while i < len(words): # Tant qu'on a pas parcouru tous les mots
                line = '' # On initialise la ligne
                while i < len(words) and font.size(line + words[i])[0] <= max_width: # Tant qu'on a pas parcouru tous les mots et que la ligne ne dépasse pas la largeur max
                    line = line + words[i] + " " # On ajoute le mot à la ligne
                    i += 1 # On passe au mot suivant
                if not line: # Si la ligne est vide 
                    line = words[i] # On ajoute le mot quand même
                    i += 1 # On passe au mot suivant
                lines.append(line) # On ajoute la ligne à la liste des lignes
        return lines # On retourne la liste des lignes

    #affcihage de la question
    lines = wrap_text(current.question, font, 500) # On découpe la question en plusieurs lignes
    y_text = button_y - 350 # On place le texte au dessus des boutons
    for line in lines: 
        text = font.render(line, True, WHITE) 
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, y_text)) # Création du rectangle englobant
        window.blit(text, text_rect) 
        y_text += 30 # On décale le texte d'une ligne
    

    # Affichage des boutons
    pg.draw.rect(window, DARK_GRAY, button_left)
    window.blit(text_left, text_rect_left)

    pg.draw.rect(window, DARK_GRAY, button_right)
    window.blit(text_right, text_rect_right)

    # Mise à jour de la fenêtre
    pg.display.flip()

# Fermeture de pygame
pg.quit()



