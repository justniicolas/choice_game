from tree import *

print(current.question)
while True:
    """Boucle principale du jeu"""
    user_choice: int = int(input("Quelle option choisissez-vous ? ")) # On demande à l'utilisateur de choisir une option
    if user_choice == 1:
        print("Vous avez choisi l'option 1")
        current = current.c1 # current.c1 est un Node
        print(current.question)
    elif user_choice == 2: 
        print("Vous avez choisi l'option 2")
        current = current.c2 # current.c2 est un Node
        print(current.question)
    else:
        print("Choix invalide, veuillez réessayer")
    if current.c1 is None and current.c2 is None: # Si les deux choix sont None, c'est que le jeu est fini
        print("Fin du jeu")
        exit()