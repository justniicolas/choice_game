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

# Final nodes
end_node = Node("Fin de l'histoire.")
escape_node = Node("Félicitations ! Vous avez réussi à quitter l'île et vous êtes sauvé. Fin de l'histoire.")

# Branches de l'histoire
build_raft = Node(
    "Vous décidez de construire un radeau pour quitter l'île. \n\
    Que faites-vous ? \n\
        [1] Vous cherchez des matériaux pour construire votre radeau. \n\
        [2] Vous essayez de trouver un autre moyen de quitter l'île."
)
build_raft.setChoice(1, escape_node)
build_raft.setChoice(2, end_node)

rescue_plane = Node(
    "Vous apercevez un avion de sauvetage à l'horizon. \n\
    Que faites-vous ? \n\
        [1] Vous allumez un feu de détresse pour attirer l'attention de l'avion. \n\
        [2] Vous agitez les bras pour essayer d'attirer l'attention de l'avion."
)
rescue_plane.setChoice(1, escape_node)
rescue_plane.setChoice(2, end_node)

meet_other_survivors = Node(
    "Vous rencontrez d'autres survivants sur l'île. \n\
    Que faites-vous ? \n\
        [1] Vous décidez de travailler ensemble pour trouver un moyen de quitter l'île. \n\
        [2] Vous continuez à explorer l'île seul."
)
meet_other_survivors.setChoice(1, build_raft)
meet_other_survivors.setChoice(2, rescue_plane)

wild_animal_encounter = Node(
    "Vous tombez nez à nez avec un animal sauvage ! \n\
    Que faites-vous ? \n\
        [1] Vous essayez de vous défendre avec votre couteau. \n\
        [2] Vous grimpez dans un arbre pour échapper à l'animal."
)
wild_animal_encounter.setChoice(1, meet_other_survivors)
wild_animal_encounter.setChoice(2, rescue_plane)

discover_cave = Node(
    "Vous découvrez une mystérieuse grotte. \n\
    Que faites-vous ? \n\
        [1] Vous explorez la grotte. \n\
        [2] Vous décidez de ne pas entrer dans la grotte et de continuer à explorer l'île."
)
discover_cave.setChoice(1, wild_animal_encounter)
discover_cave.setChoice(2, rescue_plane)

find_map = Node(     
    "Vous trouvez une carte qui semble indiquer la présence d'un trésor caché. \n\
    Que faites-vous ? \n\
        [1] Vous suivez la carte à la recherche du trésor. \n\
        [2] Vous ignorez la carte et continuez à chercher."
)

find_map.setChoice(1, discover_cave)
find_map.setChoice(2, meet_other_survivors)

explore_island = Node(
    "Vous décidez d'explorer l'île. \n\
    Que faites-vous ? \n\
        [1] Vous partez en direction de la forêt. \n\
        [2] Vous suivez la plage pour explorer les environs."
)
explore_island.setChoice(1, find_map)
explore_island.setChoice(2, wild_animal_encounter)

build_shelter = Node(
    "Vous décidez de construire un abri pour vous protéger. \n\
    Que faites-vous ensuite ? \n\
        [1] Vous partez à la recherche de nourriture. \n\
        [2] Vous explorez l'île pour en savoir plus sur votre situation."
)
build_shelter.setChoice(1, meet_other_survivors)
build_shelter.setChoice(2, explore_island)

root = Node(
    "\n \nVous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \n\
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \n\
    Que faites-vous ? \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets \n"
)
root.setChoice(1, build_shelter)
root.setChoice(2, explore_island)

def display_story(node):
    while node is not None:
        print(node.getText())
        choice = int(input("Entrez le numéro de votre choix: "))
        node = node.getNextNode(choice)

if __name__ == "__main__":
    display_story(root)
    

    
# add: tree size and height 
def tree_size_height(node):
    if node is None:
        return 0, 0

    max_height = 0
    total_size = 1

    for _, child_node in node.choices.items():
        child_size, child_height = tree_size_height(child_node)
        total_size += child_size
        max_height = max(max_height, child_height)

    return total_size, max_height + 1


size, height = tree_size_height(root)
print(f"La taille de l'arbre est {size} et sa hauteur est {height}.")
