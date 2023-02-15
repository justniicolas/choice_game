import pygame as pg

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
    "Vous allez vers la mer et vous trouvez des poissons. Vous décidez de les mettre dans votre inventaire. Mais sur le chemin de votre exploration vous trouvez une carte de l'ile. \n\
    Que faites-vous ?\n\
        [1] Vous allez sur le point le plus haut de l'ile pour marquer un message d'alerte.\n\
        [2] Vous prenez la carte et vous continuez votre exploration.\n\ "
)
construire_abri_choice = Node("Vous prenez le matériel et vous vous mettez à construire votre abri de survie. Il vous prend plusieurs heures, mais vous êtes enfin installé et en sécurité. Vous décidez alors d'explorer les alentours pour trouver des ressources.\n\
    Où allez-vous ?\n\
        [1] Vous allez vers la mer pour trouver des poissons.\n\
        [2] Vous allez vers la forêt pour explorer l'ile mais vous oubliez votre sac.\n\ "
)
construire_abri_choice.setChoice(1, take_mer_poisson)
construire_abri_choice.setChoice(2, take_take_foret)

recherche_choice= Node(
    "Vous partez à la recherche de ressources. Après avoir marché un moment, vous tombez sur un cours d'eau et décidez de vous installer pour la nuit. La nuit se passe sans encombre et le lendemain, vous reprenez votre exploration. En chemin, vous trouvez une baie remplie de coquillages et décidez de vous arrêter pour en récolter."
    "Que faites-vous ?\n\
        [1] Vous prenez les coquillages \n\
        [2] Vous êtes attirer par un bruit et vous vous éloignez du cours d'eau pour voir ce qui se passe. \n\ "
)
recherche_choice.setChoice(1, take_none)
recherche_choice.setChoice(2, take_none)

left_choice = Node(
    "Vous avez trouvé un couteau, un stylo et une trousse de secours autour du pilote. \n\
    Que faites-vous ?\n\
        1. Vous prenez le couteau et la trousse de secours. \n\
        2. Vous ne prenez rien car cela ne vous intéresse pas."
)
left_choice.setChoice(1, recherche_choice)
left_choice.setChoice(2, take_none)

# Histoire si choix = 2

take_take_foret = Node(
    "Vous allez vers la forêt et vous trouvez des fruits. Vous décidez de les mettre dans votre inventaire. Mais sur le chemin vous tombez sur un ours, mais comme vous avez oublié votre sac vous mourrez \n\" GAME OVER \ "
    )
right_choice = Node(
    "Vous prenez le colis sur la plage et vous trouvez du matériel pour faire un abri de survie. \n\
        Que faites-vous ? \n\
        [1] Vous prenez le matériel pour faire un abri de survie. \n\
        [2] Vous ne prenez rien car cela ne vous intéresse pas."
)
right_choice.setChoice(1, construire_abri_choice)
right_choice.setChoice(2, take_none)



root = Node(
    
    "\n \nVous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \n\
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \n\
    Que faites-vous ? \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets \n \n"
)
root.setChoice(1, left_choice) 
root.setChoice(2, right_choice)

current: Node = root


        