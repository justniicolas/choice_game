class Node:
    def __init__(self, question: str, c1=None, c2=None):
        self.question = question
        self.c1 = c1
        self.c2 = c2

    def setChoice(self, choice, question):
        if choice == 1:
            self.c1 = question
        else:
            self.c2 = question


root = Node(
    "Vous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \n\
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \n\
    Vous pouvez : \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets"
)
root.setChoice(1, Node("Corps"))
root.setChoice(2, Node("fouiller colis"))

current: Node = root
