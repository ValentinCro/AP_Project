import random
from Neuron import *

# La classe Player permet de définir une classe mère, peut importe le type de 
# joueur, qu'il soit humain ou qu'il soit informatique.
class Player:
    # Constructeur de la classe Player permettant l'initialisation du nom du 
    # joueur et son nombre de victoires.
    def __init__(self,name):
        self.name = name
        self.nbWin = 0
        
    # geName est un accesseur qui permet de récupérer le nom du joueur.
    def getName(self):
        return self.name
    
    # getNbWin permet de retourner le nombre de victoires du joueur.
    def getNbWin(self):
        return self.nbWin
        
    # addWin permet d'incrémenter le nombre de victoires du joueur.
    def addWin(self):
        self.nbWin+=1
    
    # addLoss permet d'avoir la méthode au cas ou on souhaite effectuer un 
    # traitement plus tard.
    def addLoss(self):
        pass

# La classe HumanPlayer permet de créer un objet contenant les informations d'un
# joueur humain.
class HumanPlayer(Player):
    
    # La méthode play permet de récupérer l'entrée utilisateur et d'effectuer le
    # traitement nécessaire au cas ou ce dernier entre des données incorrect.
    # Par exemple, impossible pour l'utilisateur de rentrer un entier inférieur 
    # à 1 ou supérieur à 3.
    def play(self,sticks):
        if sticks==1: return 1
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n')
                try:
                    nb=int(nb)
                    if nb>=1 and nb<=3 and sticks-nb>=0:
                        correct=True
                except: pass
            return nb

# La classe CPUPlayer permet de créer un objet contenant les informations d'un 
# joueur informatique.
class CPUPlayer(Player):
    
    # Le constructeur de la classe CPUPlayer permet d'initialiser l'objet avec 
    # des attributs qui sont le nom, la complexité de l'algorithme régissant 
    # l'intelligence artificielle et le nombre de sticks permettant à 
    # l'algorithme hard d'effectuer les traitements nécessaire dans le réseau 
    # de neurone.
    def __init__(self,name,mode,nbSticks):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(3,nbSticks)
        self.previousNeuron = None
        
    # La méthode play permet au joueur informatique de jouer en fonction de 
    # la compléxité choisie. Dans le même cas que pour un joueur humain, cette 
    # méthode retourne un entier entre 1 et 3 inclu.
    def play(self,sticks):
        if self.mode=='easy': return self.playEasy(sticks)
        elif self.mode=='hard': return self.playHard(sticks)
        else: return self.playMedium(sticks)
        
    # La méthode playMedium permet à l'ordinateur de jouer en aléatoire, sauf 
    # en cas de victoire possible où là un petit algorithme prend le relai pour 
    # augmenter les chances de victoire de l'ordinateur.
    def playMedium(self,sticks):
        # TODO compléter ici avec les quelques conditions pour éviter de faire une grosse erreur aux derniers tours
        return self.playRandom(sticks)
        
    # La méthode playEasy permet à l'ordinateur de jouer. Cette méthode retourne
    # tout simplement un nombre aléatoire entre 1 et 3 grâce à la méthode
    # playRandom.
    def playEasy(self,sticks):
        return self.playRandom(sticks)
    
    # La méthode playRandom permet de retourner un entier entre 1 et 3
    def playRandom(self,sticks):
        return random.randint(1, (sticks%3)+1)
        
    # La méthode playHard permet de retourner un entier entre 1 et 3 
    # avec toute une intelligence artificielle derrière le choix de cet entier.
    def playHard(self,sticks):
        # TODO utiliser le réseau neuronal pour choisir le nombre de bâtons à jouer
        # utiliser l'attribut self.previousNeuron pour avoir le neuron précédemment sollicité dans la partie
        # calculer un 'shift' qui correspond à la différence entre la valeur du précédent neurone et le nombre de bâtons encore en jeu
        # utiliser la méthode 'chooseConnectedNeuron' du self.previousNeuron puis retourner le nombre de bâtons à jouer
        # bien activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible
        # attention à gérer les cas particuliers (premier tour ou sticks==1)
        return playMedium(sticks)
        
    # La méthode getNeuronNetwork permet de retourner le réseau de neurones de 
    # l'intelligence artificielle.
    def getNeuronNetwork(self): return self.netw
    
    # La méthode addWin permet d'incrémenter le nombre de victoire du joueur.
    # Elle permet également de réinitialiser l'état de l'intelligence.
    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron=None
        
    # La méthode addLoss permet de réinitialiser l'état de l'intelligence 
    # artificielle.
    def addLoss(self):
        super().addLoss()
        self.previousNeuron=None




        


