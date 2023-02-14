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

take_none = Node("Vous avez choisi de ne rien prendre. Vous attendez les secours et vous mourrez de faim. Merci d'avoir joué !", None, None)


take_nourriture = Node("Vous avez choisi de prendre le couteau pour aller chercher de la nourriture. Vous vous promener *longtemps* et vous trouvez un poisson mais vous vous rendez compte que ce poisson est . Que faites-vous ? 1. Vous le mangez. 2. Vous ne le mangez pas car vous n'avez pas d'eau.", take_none, take_none)

take_couteau = Node("Vous avez choisi de prendre le couteau et la trousse de secours. Vous avez faim et vous n'avez pas d'eau. Que faites-vous ? 1. Vous prenez le couteau pour aller chercher de la nourriture. 2. Vous ne prenez rien car cela ne vous intéresse pas.", take_nourriture, take_none)

left_choice = Node("Vous avez trouvé un couteau, un stylo et une trousse de secours autour du pilote. Que faites-vous ? 1. Vous prenez le couteau et la trousse de secours. 2. Vous ne prenez rien car cela ne vous intéresse pas.", take_couteau, take_none)

take_tuetigre = Node("Vous avez choisi de tuer le tigre. Vous avez réussi à le tuer mais vous vous êtes blesser. Mais vous avez assez de nourriture pour pouvoir surivivre. 1. Vous vous soignez avec le matériel de la trousse de secours. 2. Vous vous faites un festin car cela fait 2 jours que vous avez rien mangé.", take_none, take_none)

take_faire_semblantdedormir = Node("Vous avez choisi de faire semblant d'être mort. Le tigre vous mange et vous êtes mort. Merci d'avoir joué !", None, None)

take_recherchebois = Node("Vous avez choisir de tracer votre chemin. Vous vous promener et vous prenez votre bois pour continuer votre campement. Vous vous endormez et vous vous réveillez le lendemain en tête à tête avec un tigre. Que faites vous ? 1. Vous faites semblant d'etre mort. 2.Vous prenez votre couteau et vous le tuez.", take_faire_semblantdedormir, take_tuetigre)

take_betesauvage = Node("Vous avez choisi de caresser la petite bête. Elle vous mord et vous êtes mort. Merci d'avoir joué !", None, None)

take_feu = Node("Vous avez choisi de prendre le couteau pour aller chercher du bois. Vous vous promener *longtemps* et vous tombez sur une petite bête sauvage mignonne. Que faites-vous ? 1. Vous tracez votre chemin. 2. Vous décidez de caresser la petite bête.", take_betesauvage, take_recherchebois)

take_abri = Node("Vous avez choisi de prendre le matériel pour faire un abri de survie mais vous n'avez pas de feu. Que faites-vous ? 1. Vous prenez le couteau qui est dans le colis pour aller chercher du bois. 2. Vous vous dites que vous ferez ça demain car vous êtes fatigués et vous commencez votre abri fais à base de boite en carton qui risque de s'effondrer au premier coup de vent.", take_feu, take_none)

right_choice = Node(
    "Vous prenez le colis sur la plage et vous trouvez du matériel pour faire un abri de survie. \n\
        Que faites-vous ? \n\
        [1] Vous prenez le matériel pour faire un abri de survie. \n\
        [2] Vous ne prenez rien car cela ne vous intéresse pas.", take_abri, take_none
        )
        
root = Node(
    "Vous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \n\
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \n\
    Que faites-vous ? \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets"
)
root.setChoice(1, Node("Corps"))
root.setChoice(2, Node("Fouiller colis"))

current: Node = root
