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
take_none = Node("Le jeu est pas fini", None, None)


left_choice = Node(
    "Vous avez trouvé un\n\
        1. Vous prenez le couteau et la trousse de secours. \n\
        2. Vous ne prenez rien car cela ne vous intéresse pas."
)
left_choice.setChoice(1, take_none)
left_choice.setChoice(2, take_none)
# Histoire si choix = 2

right_choice = Node(
    "Vous prenez \n\
        [1] Vous prenez le matériel pour faire un abri de survie. \n\
        [2] Vous ne prenez rien car cela ne vous intéresse pas."
)
right_choice.setChoice(1, take_none)
right_choice.setChoice(2, take_none)
root = Node(
    
    "\n \nVous êtes co-pilote \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets \n \n"
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
button_y = (WINDOW_HEIGHT - (2 * button_height + button_margin)) / 2 # On centre le bouton

# Bouton gauche
button_left = pg.Rect(button_x, button_y, button_width, button_height) # Création du rectangle
text_left = font.render("Choix 1", True, WHITE) 
text_rect_left = text_left.get_rect(center=button_left.center) # Création du rectangle englobant

# Bouton droit
button_right = pg.Rect(button_x, button_y + button_height + button_margin, button_width, button_height) # Création du rectangle
text_right = font.render("Choix 2", True, WHITE)
text_rect_right = text_right.get_rect(center=button_right.center) # Création du rectangle englobant

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

    def wrap_text(text, font, max_width):
        """Méthode permettant de découper un texte en plusieurs lignes si sa longueur dépasse max_width"""
        words = text.split(' ')
        lines = []
        current_line = words[0]
        for word in words[1:]:
            if font.size(current_line + ' ' + word)[0] <= max_width: # Si la longueur du texte actuel + le mot actuel est inférieure à max_width
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        return '\n'.join(lines)

    # Création de l'objet text_question pour afficher la question actuelle
    text_question = font.render(wrap_text(current.question, font, WINDOW_WIDTH), True, BLACK)


    # Calcul du rectangle englobant de text_question pour centrer le texte sur la fenêtre
    text_rect_question = text_question.get_rect() # Création du rectangle englobant
    text_rect_question.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4)  # Centrage du rectangle englobant

    # Affichage de text_question sur la fenêtre
    window.blit(text_question, text_rect_question)  

    # Affichage des boutons
    pg.draw.rect(window, DARK_GRAY, button_left)
    window.blit(text_left, text_rect_left)

    pg.draw.rect(window, DARK_GRAY, button_right)
    window.blit(text_right, text_rect_right)

    # Mise à jour de la fenêtre
    pg.display.flip()

# Fermeture de pygame
pg.quit()



