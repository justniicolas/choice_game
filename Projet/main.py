class Node:
    def __init__(self, story_piece, choice_a, choice_b):
        self.story_piece = story_piece
        self.choice_a = choice_a
        self.choice_b = choice_b

take_none = Node("Vous avez choisi de ne rien prendre. Vous attendez les secours et vous mourrez de faim. Merci d'avoir joué !", None, None)




take_couteau = Node("Vous avez choisi de prendre le couteau et la trousse de secours. Vous avez faim et vous n'avez pas d'eau. Que faites-vous ? 1. Vous prenez le couteau pour aller chercher de la nourriture. 2. Vous ne prenez rien car cela ne vous intéresse pas.", take_nourriture, take_none)

left_choice = Node("Vous avez trouvé un couteau, un stylo et une trousse de secours autour du pilote. Que faites-vous ? 1. Vous prenez le couteau et la trousse de secours. 2. Vous ne prenez rien car cela ne vous intéresse pas.", take_couteau, take_none)





take_abri = Node("Vous avez choisi de prendre le matériel pour faire un abri de survie mais vous n'avez pas de feu. Que faites-vous ? 1. Vous prenez le couteau qui est dans le colis pour aller chercher du bois. 2. Vous vous dites que vous ferez ça demain car vous êtes fatigués.", take_feu, take_none)

right_choice = Node("Vous prenez le colis sur la plage et vous trouvez du matériel pour faire un abri de survie. Que faites-vous ? 1. Vous prenez le matériel pour faire un abri de survie. 2. Vous ne prenez rien car cela ne vous intéresse pas.", take_abri, take_none)


story_root = Node("Vous êtes rescaper d'un crash d'avion. Vous êtes seul sur la plage après avoir nager jusqu'à une île. Vous regardez autour de vous et vous voyez le corps d'un des pilotes et un colis sur la plage Que faites-vous ? 1. Vous allez fouiller le corps du pilote dans l'eau 2. Vous allez fouiller le colis sur la plage pour essayer de récuperer des objets en attendant les secours", left_choice, right_choice)



current_node = story_root
while True : 
    print(current_node.story_piece)
    user_choice = input("Entre 1 ou 2 pour continuer l'aventure: ")
    if user_choice == "1":
        current_node = current_node.choice_a
    elif user_choice == "2":
        current_node = current_node.choice_b
    elif user_choice != "1" or "2":
        print("Merci de choisir 1 ou 2")
    



