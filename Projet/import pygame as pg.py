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
    "Vous avez trouvé un 1. Vous prenez le couteau et la trousse de secours. 2. Vous ne prenez rien car cela ne vous intéresse pas."
)
left_choice.setChoice(1, take_none)
left_choice.setChoice(2, take_none)
# Histoire si choix = 2

right_choice = Node(
    "Vous prenez [1] Vous prenez le matériel pour faire un abri de survie.[2] Vous ne prenez rien car cela ne vous intéresse pas."
)
right_choice.setChoice(1, take_none)
right_choice.setChoice(2, take_none)
root = Node(
    
    "Vous êtes co-pilote [1]Fouiller le corps du pilote pour récupérer des objets [2]Fouiller les colis sur la plage pour récupérer des objets"
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
        if font.size(text)[0] <= max_width:
            lines.append(text)
        else:
            words = text.split(' ')
            i = 0
            while i < len(words):
                line = ''
                while i < len(words) and font.size(line + words[i])[0] <= max_width:
                    line = line + words[i] + " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines

    #affcihage de la question
    lines = wrap_text(current.question, font, 500)
    y_text = button_y - 100
    for line in lines:
        text = font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, y_text))
        window.blit(text, text_rect)
        y_text += 30
    

    # Affichage des boutons
    pg.draw.rect(window, DARK_GRAY, button_left)
    window.blit(text_left, text_rect_left)

    pg.draw.rect(window, DARK_GRAY, button_right)
    window.blit(text_right, text_rect_right)

    # Mise à jour de la fenêtre
    pg.display.flip()

# Fermeture de pygame
pg.quit()



