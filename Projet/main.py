class Node:
    def __init__(self, text):
        self.text = text
        self.choices = {}

    def setChoice(self, choice_number, next_node):
        self.choices[choice_number] = next_node

    def getText(self):
        return self.text

    def getNextNode(self, choice_number):
        return self.choices.get(choice_number, None)


search_water = Node(
    "Vous trouvez une source d'eau potable en explorant l'île. \n\
    Que faites-vous ? \n\
        [1] Vous buvez de l'eau pour vous hydrater. \n\
        [2] Vous remplissez une bouteille ou un récipient pour avoir de l'eau avec vous."
)
search_water.setChoice(1, None)
search_water.setChoice(2, None)

create_distress_signal = Node(
    "Vous créez un signal de détresse avec les objets trouvés. \n\
    Que faites-vous ensuite ? \n\
        [1] Vous montez sur un arbre pour essayer de repérer des signes de civilisation. \n\
        [2] Vous construisez un feu pour attirer l'attention des secours."
)
create_distress_signal.setChoice(1, None)
create_distress_signal.setChoice(2, None)

create_distress_signal.setChoice(1, None)
create_distress_signal.setChoice(2, None)

build_shelter_beach = Node(
    "Vous construisez votre abri près de la plage. \n\
    Que faites-vous ensuite ? \n\
        [1] Vous cherchez de la nourriture sur la plage. \n\
        [2] Vous vous reposez dans votre abri."
)
build_shelter_beach.setChoice(1, None)
build_shelter_beach.setChoice(2, None)

explore_island = Node(
    "Vous explorez l'intérieur de l'île pour trouver un meilleur endroit pour construire votre abri. \n\
    Que faites-vous ensuite ? \n\
        [1] Vous découvrez une grotte et décidez d'y construire votre abri. \n\
        [2] Vous trouvez un endroit abrité au pied d'une colline et décidez d'y construire votre abri."
)
explore_island.setChoice(1, None)
explore_island.setChoice(2, None)

# Histoire si choix = 1 et sous-choix = 1

take_knife_medkit = Node(
    "Vous prenez le couteau et la trousse de secours. Avec ces objets en main, vous pouvez maintenant prendre soin de vous et vous défendre en cas de besoin. \n\
    Que faites-vous ensuite ? \n\
        [1] Vous partez à la recherche d'eau potable. \n\
        [2] Vous essayez de créer un signal de détresse avec les objets trouvés."
)
take_knife_medkit.setChoice(1, search_water)
take_knife_medkit.setChoice(2, create_distress_signal)

# Histoire si choix = 1

left_choice = Node(
    
    "Vous avez trouvé un couteau, un stylo et une trousse de secours autour du pilote. \n\
        Que faites-vous ? \n\
            [1] Vous prenez le couteau et la trousse de secours. \n\
            [2] Vous ne prenez rien car cela ne vous intéresse pas."
)


left_choice.setChoice(1, take_knife_medkit)
left_choice.setChoice(2, None)

# Histoire si choix = 2 et sous-choix = 1

take_shelter_material = Node(
    "Vous prenez le matériel pour faire un abri de survie. Avec ces objets, vous pouvez maintenant construire un abri pour vous protéger des intempéries. \n\
    Que faites-vous ensuite ? \n\
        [1] Vous construisez votre abri près de la plage. \n\
        [2] Vous explorez l'intérieur de l'île pour trouver un meilleur endroit pour construire votre abri."
)
take_shelter_material.setChoice(1, build_shelter_beach)
take_shelter_material.setChoice(2, explore_island)

# Histoire si choix = 2

right_choice = Node(
    "Vous prenez le colis sur la plage et vous trouvez du matériel pour faire un abri de survie. \n\
        Que faites-vous ? \n\
        [1] Vous prenez le matériel pour faire un abri de survie. \n\
        [2] Vous ne prenez rien car cela ne vous intéresse pas."
)
right_choice.setChoice(1, take_shelter_material)
right_choice.setChoice(2, None)

root = Node(
    "\n \nVous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \n\
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \n\
    Que faites-vous ? \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets \n"
)
root.setChoice(1, left_choice)
root.setChoice(2, right_choice)


def display_story(node):
    while node is not None:
        print(node.getText())
        choice = int(input("Entrez le numéro de votre choix: "))
        node = node.getNextNode(choice)


if __name__ == "__main__":
    display_story(root)