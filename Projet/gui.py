import webbrowser
import pygame as pg


class Node:
    """Classe représentant un noeud de l'arbre de décision."""

    def __init__(self, text, update_life=0, update_inventory=None):
        """Constructeur de la classe Node."""
        self.text = text
        self.choices = {}
        self.update_life = update_life
        self.update_inventory = update_inventory or {}

    def setChoice(self, choice_number, next_node):
        """Ajoute un choix à la liste des choix possibles."""
        self.choices[
            choice_number
        ] = next_node  # On ajoute le choix à la liste des choix possibles

    def getText(self):
        """Retourne le texte du noeud."""
        return self.text  # On retourne le texte du noeud

    def getNextNode(self, choice_number):
        """Retourne le noeud suivant en fonction du choix de l'utilisateur."""
        return self.choices.get(choice_number, None)

    def is_valid_choice(self, choice_number):
        """Retourne True si le choix est valide, False sinon."""
        return (
            choice_number in self.choices
        )  # On vérifie si le choix est dans la liste des choix possibles


class Player:
    def __init__(self) -> None:
        self.health = 50
        self.inventory = {}

    def apply_changes(self, hp, inv):
        """Applique les changements de vie et d'inventaire."""
        self.health += (
            hp  # On ajoute la valeur de la modification de vie à la vie actuelle
        )
        self.health = min(self.health, 100)  # On limite la vie à 100
        # Pour chaque item dans le dictionnaire des changements d'inventaire
        for item, count in inv.items():
            # On ajoute la quantité de l'item à l'inventaire
            self.inventory[item] = self.inventory.get(item, 0) + count
            if self.inventory[item] <= 0:
                # On supprime l'item de l'inventaire si la quantité est négative ou nulle
                del self.inventory[item]

    def get_health(self):
        return self.health


player = Player()


# Final nodes
end_node = Node("Fin de l'histoire. Vous êtes mort.")
escape_node = Node(
    "Félicitations ! Vous avez réussi à quitter l'île et vous êtes sauvé. Fin de l'histoire."
)


build_raft = Node(
    "Vous avez rassemblé les matériaux nécessaires pour construire un radeau, mais il y a un problème. \
    L'île semble être entourée de requins. \
    Que faites-vous ? \
        [1] Vous construisez un radeau solide et tentez de naviguer en évitant les requins. \
        [2] Vous abandonnez l'idée du radeau et cherchez d'autres moyens de quitter l'île."
)


signal_fire = Node(
    "Vous avez réussi à allumer un feu de détresse, mais la pluie commence à tomber. \
    Que faites-vous ? \
        [1] Vous protégez le feu avec votre corps et espérez que l'avion vous voit. \
        [2] Vous abandonnez le feu et essayez de trouver un autre moyen de signaler votre présence."
)


climbing_mountain = Node(
    "Vous décidez de gravir la montagne pour avoir une meilleure vue de l'île et chercher un moyen de quitter l'île. \
    Que faites-vous ? \
        [1] Vous escaladez la montagne avec précaution, en utilisant tout votre équipement. \
        [2] Vous décidez que l'escalade est trop risquée et cherchez un autre moyen de quitter l'île."
)
rescue_plane = Node(
    "Vous apercevez un avion de secours au loin. \
    Que faites-vous ? \
        [1] Vous utilisez un miroir pour refléter la lumière du soleil et attirer l'attention de l'avion. \
        [2] Vous allumez un feu de détresse sur la plage pour signaler votre présence."
)

wild_animal_encounter = Node(
    "Vous êtes confronté à un animal sauvage, et votre couteau se brise pendant le combat. \
    Que faites-vous ? \
        [1] Vous utilisez vos compétences en arts martiaux pour combattre l'animal. \
        [2] Vous essayez de fuir et de trouver un endroit sûr pour vous cacher."
)
meet_other_survivors = Node(
    "Vous rencontrez d'autres survivants sur l'île. \
    Que faites-vous ? \
        [1] Vous décidez de travailler ensemble pour trouver un moyen de quitter l'île. \
        [2] Vous continuez à explorer l'île seul."
)

discover_cave = Node(
    "Vous découvrez une mystérieuse grotte qui semble mener à un réseau souterrain. \
    Que faites-vous ? \
        [1] Vous explorez prudemment le réseau souterrain, en suivant les marques laissées par d'autres explorateurs. \
        [2] Vous décidez que le réseau souterrain est trop dangereux et continuez à chercher un moyen de quitter l'île."
)


find_map = Node(
    "Vous trouvez une carte qui semble indiquer la présence d'un trésor caché, mais elle est partiellement détruite. \
    Que faites-vous ? \
        [1] Vous essayez de déchiffrer la carte et de suivre les indices restants. \
        [2] Vous ignorez la carte et continuez à chercher un moyen de quitter l'île."
)


explore_island = Node(
    "Vous décidez d'explorer l'île, mais vous découvrez que le terrain est difficile et dangereux. \
    Que faites-vous ? \
        [1] Vous partez en direction de la forêt, en affrontant les dangers qui s'y trouvent. \
        [2] Vous suivez la plage pour explorer les environs, en évitant les zones dangereuses."
)


build_shelter = Node(
    "Vous décidez de construire un abri pour vous protéger, mais vous vous rendez compte que les matériaux sont limités. \
    Que faites-vous ensuite ? \
        [1] Vous partez à la recherche de nourriture, en prenant des risques pour trouver des ressources. \
        [2] Vous explorez l'île pour en savoir plus sur votre situation, malgré les dangers potentiels."
)


root = Node(
    "Vous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \
    Que faites-vous ? \
        [1] Fouiller le corps du pilote pour récupérer des objets \
        [2] Fouiller les colis sur la plage pour récupérer des objets ",
)

# Liaison des choix
root.setChoice(1, build_shelter)
root.setChoice(2, explore_island)

build_shelter.setChoice(1, meet_other_survivors)
build_shelter.setChoice(2, explore_island)

explore_island.setChoice(1, find_map)
explore_island.setChoice(2, wild_animal_encounter)

find_map.setChoice(1, discover_cave)
find_map.setChoice(2, signal_fire)

discover_cave.setChoice(1, wild_animal_encounter)
discover_cave.setChoice(2, signal_fire)

wild_animal_encounter.setChoice(1, meet_other_survivors)
wild_animal_encounter.setChoice(2, rescue_plane)

meet_other_survivors.setChoice(1, build_raft)
meet_other_survivors.setChoice(2, rescue_plane)

rescue_plane.setChoice(1, escape_node)
rescue_plane.setChoice(2, escape_node)

build_raft.setChoice(1, escape_node)
build_raft.setChoice(2, explore_island)

signal_fire.setChoice(1, escape_node)
signal_fire.setChoice(2, explore_island)

# Ajout d'objets aux noeuds
root.update_inventory = {"montre": 1, "couteau": 1}
root.update_life = -5
build_shelter.update_inventory = {"bois": 5, "corde": 2, "nourriture": 10}
build_shelter.update_life = -10
explore_island.update_inventory = {"boussole": 1}
explore_island.update_life = -5
find_map.update_inventory = {"carte_au_tresor": 1}
find_map.update_life = 10
discover_cave.update_inventory = {"torche": 1}
wild_animal_encounter.update_inventory = {"couteau": 1}
wild_animal_encounter.update_life = -35
meet_other_survivors.update_inventory = {"nourriture": -4, "chaussures": 2}
meet_other_survivors.update_life = 5
rescue_plane.update_inventory = {"miroir": 1}
rescue_plane.update_life = -5
build_raft.update_inventory = {"bois": 10, "corde": 5, "voile": 1}
build_raft.update_life = -10

current: Node = root


# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Taille de la fenêtre
WINDOW_WIDTH = 1200
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
button_x = (WINDOW_WIDTH - button_width) / 2  # On centre le bouton
button_y = (
    WINDOW_HEIGHT - (5 * button_height + button_margin)
) - 50  # On place le bouton en bas de la fenêtre

# Bouton gauche
button_left = pg.Rect(
    button_x - button_width / 2 - button_margin,
    button_y + 200,
    button_width,
    button_height,
)  # Création du rectangle
text_left = font.render("Choix 1", True, WHITE)
text_rect_left = text_left.get_rect(
    center=button_left.center
)  # Création du rectangle englobant

# Bouton droit
button_right = pg.Rect(
    button_x + button_width / 2 + button_margin,
    button_y + 200,
    button_width,
    button_height,
)  # Création du rectangle
text_right = font.render("Choix 2", True, WHITE)
text_rect_right = text_right.get_rect(
    center=button_right.center
)  # Création du rectangle englobant

# Bouton pour démarrer le jeu
button_start = pg.Rect(button_x, button_y, button_width, button_height)
text_start = font.render("Commencer le jeu", True, WHITE)
text_rect_start = text_start.get_rect(center=button_start.center)

# Bouton pour ouvrir le repo
button_repo = pg.Rect(
    button_x, button_y + button_height + button_margin, button_width, button_height
)
text_repo = font.render("Code source", True, WHITE)
text_rect_repo = text_repo.get_rect(center=button_repo.center)

# TODO Bouton pour afficher les regles
button_rules = pg.Rect(
    button_x,
    button_y + 2 * (button_height + button_margin),
    button_width,
    button_height,
)
text_rules = font.render("Règles", True, WHITE)
text_rect_rules = text_rules.get_rect(center=button_rules.center)

# Bouton pour quitter le jeu
button_quit = pg.Rect(
    button_x,
    button_y + 3 * (button_height + button_margin),
    button_width,
    button_height,
)
text_quit = font.render("Quitter le jeu", True, WHITE)
text_rect_quit = text_quit.get_rect(center=button_quit.center)

text_menu = font.render("Menu", True, WHITE)
text_rect_menu = text_menu.get_rect(center=(WINDOW_WIDTH / 2, 200))

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

            elif button_repo.collidepoint(mouse_pos):
                webbrowser.open("https://github.com/justniicolas/choice_game")

    # Couleur de fond de la fenêtre
    window.fill(GRAY)

    # Affichage des boutons
    pg.draw.rect(window, DARK_GRAY, button_start, 2, 3)
    window.blit(text_start, text_rect_start)

    pg.draw.rect(window, DARK_GRAY, button_quit, 2, 3)
    window.blit(text_quit, text_rect_quit)

    pg.draw.rect(window, DARK_GRAY, button_repo, 2, 3)
    window.blit(text_repo, text_rect_repo)

    pg.draw.rect(window, DARK_GRAY, button_rules, 2, 3)
    window.blit(text_rules, text_rect_rules)

    window.blit(text_menu, text_rect_menu)

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
            if button_left.collidepoint(mouse_pos):
                player.apply_changes(current.update_life, current.update_inventory)
                current = current.getNextNode(1)
                print(current.getText)

            # Si le bouton droit est cliqué
            elif button_right.collidepoint(mouse_pos):
                player.apply_changes(current.update_life, current.update_inventory)
                current = current.getNextNode(2)
                print(current.getText())

    # Couleur de fond de la fenêtre
    window.fill(GRAY)

    # methode permettant de couper la question en plusieurs lignes
    def wrap_text(text, font, max_width):
        lines = []
        text = text.split("[")
        if font.size(text[0])[0] <= max_width:  # Si le texte tient sur une ligne
            lines.append(text)  # On ajoute la ligne
        else:
            words = text[0].split(" ")  # On découpe le texte en mots
            i = 0  # Compteur de mots
            while i < len(words):  # Tant qu'on a pas parcouru tous les mots
                line = ""  # On initialise la ligne
                while (
                    i < len(words) and font.size(line + words[i])[0] <= max_width
                ):  # Tant qu'on a pas parcouru tous les mots et que la ligne ne dépasse pas la largeur max
                    line = line + words[i] + " "  # On ajoute le mot à la ligne
                    i += 1  # On passe au mot suivant
                if not line:  # Si la ligne est vide
                    line = words[i]  # On ajoute le mot quand même
                    i += 1  # On passe au mot suivant
                lines.append(line)  # On ajoute la ligne à la liste des lignes
        return lines  # On retourne la liste des lignes

    # TODO Affichage de la barre de vie ?
    # health = player.get_health()
    # print(health)
    # * Bon on le fera peut-être après jsp

    # affcihage de la question
    if current.getText() is not None:
        button_y = 450
        lines = wrap_text(
            current.getText(), font, 500
        )  # On découpe la question en plusieurs lignes
        y_text = button_y - 350  # On place le texte au dessus des boutons
        for line in lines:
            if not isinstance(line, str):
                line = line[0]
            text = font.render(line, True, WHITE)
            text_rect = text.get_rect(
                center=(WINDOW_WIDTH / 2, y_text)
            )  # Création du rectangle englobant
            window.blit(text, text_rect)
            y_text += 30  # On décale le texte d'une ligne
        y_text += 60
        possible_choices = current.getText().split("[")
        for choice in possible_choices[1::]:
            text = font.render("[" + choice, True, WHITE)
            text_rect = text.get_rect(
                center=(WINDOW_WIDTH / 2, y_text)
            )  # Création du rectangle englobant
            window.blit(text, text_rect)
            y_text += 45
    else:
        text = font.render("yo", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, 500))
        window.blit(text, text_rect)

    # Affichage des boutons
    pg.draw.rect(window, DARK_GRAY, button_left, 2, 3)
    window.blit(text_left, text_rect_left)

    pg.draw.rect(window, DARK_GRAY, button_right, 2, 3)
    window.blit(text_right, text_rect_right)

    # Mise à jour de la fenêtre
    pg.display.flip()

# Fermeture de pygame
pg.quit()
