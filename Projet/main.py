from tree import *

print(current.question)
while True:
    user_choice: int = int(input("Quelle option choisissez-vous ? "))
    if user_choice == 1:
        print("Vous avez choisi l'option 1")
        current = current.c1
        print(current.question)
    elif user_choice == 2:
        print("Vous avez choisi l'option 2")
        current = current.c2
        print(current.question)
    else:
        print("Choix invalide, veuillez réessayer")
    if current.c1 is None and current.c2 is None:
        print("Fin du jeu")
        exit()