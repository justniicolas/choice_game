class Node:
    """Classe représentant un noeud de l'arbre de décision"""

    def __init__(self, question: str, c1=None, c2=None):
        self.question = question
        self.c1 = c1
        self.c2 = c2

    def setChoice(self, choice, question):
        """Méthode permettant de définir les choix possibles"""
        if choice == 1:
            self.c1 = question  # question est un Node
        else:
            self.c2 = question  # question est un Node


# EN COURS DE DEVELOPPEMENT
take_none = Node("Vous avez perdu", None, None)

# Histoire si choix = 1
construire_abri_sur_plage = Node(
    "Vous êtes entrain de construire votre abri sur la plage, mais vous entendez une voix qui appelle à l'aide. \n\
        Que faites-vous ? \n\
        [1] Vous décidez d'aller voir ce qui se passe \n\
        [2] Vous continuez à construire votre abri de survie."
)
construire_abri_sur_plage.setChoice(1, take_none)
construire_abri_sur_plage.setChoice(2, take_none)


abri_construction = Node(
    "Vous avez pris votre matériel pour construire un abri de survie. Mais vous ne savez pas où mettre votre abri \n\ "
    "Que faites-vous ? \n\
    [1] Vous décidez de construire votre abri sur la plage \n\
    [2] Vous décidez de construire votre abri dans la forêt."
)
prendre_outils = Node(
    "Vous avez pris les outils pour suivre, mais maintenant vous êtes mouiller. \n\
    Que faites_vous ? \n\
    [1] Vous décidez de faire une petite brasse coulé pour observer le paysage paradisiaque \n\
    [2] Vous retournez sur la plage pour trouver un abri de survie."
)
prendre_outils.setChoice(1, take_none)
prendre_outils.setChoice(2, abri_construction)

abri_construction.setChoice(1, construire_abri_sur_plage)
abri_construction.setChoice(2, take_none)

left_choice = Node(
    "Vous avez trouvé un couteau, un stylo et une trousse de secours autour du pilote. \n\
    Que faites-vous ?\n\
        [1] Vous prenez le couteau et la trousse de secours. \n\
        [2] Vous ne prenez rien car cela ne vous intéresse pas."
)
left_choice.setChoice(1, prendre_outils)
left_choice.setChoice(2, take_none)


# Histoire si choix = 2
construire_abri_dans_foret = Node(
    "Vous êtes entrain de construire votre abri dans la forêt, mais vous vous faites mordre par un des survivants qui est devenu un zombie. \n\ 
    Que faites-vous ? \n\
    [1] Vous vous soigner avec le matériel que vous avez pris \n\
    [2] Vous continuez à construire votre abri de survie en espérant que ca aille mieux."
)

right_choice = Node(
    "Vous prenez le colis sur la plage et vous trouvez du matériel pour faire un abri de survie. \n\
        Que faites-vous ? \n\
        [1] Vous prenez le matériel pour faire un abri de survie. \n\
        [2] Vous ne prenez rien car cela ne vous intéresse pas."
)
right_choice.setChoice(1, abri_construction)
right_choice.setChoice(2, take_none)


root = Node(
    "\n \nVous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \n\
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \n\
    Que faites-vous ? \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets \n"
)
root.setChoice(1, left_choice)
root.setChoice(2, right_choice)

current: Node = root
