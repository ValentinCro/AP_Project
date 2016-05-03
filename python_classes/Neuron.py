import random

BASE_WEIGHT = 10
RECOMPENSE = 8

# La classe NeuronNetwork permet de matérialiser un réseau de Neuron, c'est à 
# dire une collection de Neuron.
class NeuronNetwork:

    # Le constructeur de la classe NeuronNetwork permet d'initialiser le réseau
    # de Neuron avec nbSticks Neurons dans la collection.
    def __init__(self, maxDist, nbSticks):
    
        # On initialise un tableau vide qui contiendra les Neurons. C'est la 
        # collection de Neurons.
        self.neurons = []
        
        # On boucle de 1 à nbSticks+1 car la méthode range va du premier 
        # paramètre au deuxième-1
        for i in range(1, nbSticks + 1):
            # A chaque itération de boucle, on ajoute un Neuron avec comme 
            # identifiant le i actuel qui représente le nombre de sticks 
            # encore en jeu.
            self.neurons.append(Neuron(self, i))
        
        # Pour chaque Neuron présent dans la collection on effectue les 
        # connections et on initialise leur poids de base.
        for neuron in self.neurons:
            neuron.makeConnections(maxDist, nbSticks, BASE_WEIGHT)
            
        self.initPath()

    # La méthode initPath permet de créer le gestionnaire de chemins entre les 
    # neuronnes.
    def initPath(self):
        self.path = {}

    # Le méthode getNeuron permet de récupérer le neuron à l'index passé 
    # en paramètre. La méthode prends en compte le fait qu'on ne peut pas 
    # récupérer un neurone qui est en dehors de la collection. Dans le cas 
    # où on passe un index qui est en dehors de la collection, la méthode 
    # retourne None. 
    def getNeuron(self,index):
        if index - 1 >= 0 and index <= len(self.neurons): 
            return self.neurons[index - 1]
        else: 
            return None

    # La méthode activateNeuronPath permet de lier un neuronne avec un autre 
    # grâce au gestionnaire de chemins entre les neuronnes.
    def activateNeuronPath(self,neuron1,neuron2):
        self.path[neuron1]=neuron2

    # La méthode recompenseConnections permet de récompenser les connections de 
    # neuronnes qui permettent la victoire.
    def recompenseConnections(self):
        for neuron1,neuron2 in self.path.items():
            neuron1.recompenseConnection(neuron2)
        # On réinitialise le gestionnaire de chemins.
        self.initPath()

    # La méthode printAllConnections permet d'afficher toutes les connections.
    def printAllConnections(self):
        for neuron in self.neurons: neuron.printConnections() 

    # La méthode printScores permet d'afficher le score des neuronnes.
    def printScores(self):
        scores = {}
        for neuron in self.neurons:
            for n,s in neuron.connections.items():
                if n not in scores: scores[n]=s
                else: scores[n] = scores[n] + s
        for neuron,score in scores.items():
            print(neuron.asString(), score)


# La classe Neuron représente un neurone. Cet objet contient le réseau neuronal,
# un identifiant de neuron (ici des entiers correspondant au nombre de sticks) 
# et un ensemble de connections vers d'autres neurones.
class Neuron:

    # Le constructeur de la classe Neuron permet d'initialiser le Neuron courant
    # en lui indiquant le réseau de neurones auquel il appartient et son index (
    # c'est à dire son identifiant dans le réseau de neurones).
    def __init__(self, network, index):
        self.network = network
        self.index = index
        self.connections = {}

    # La méthode makeConnections permet de faire la connection entre les 
    # neurones. 
    def makeConnections(self, maxDist, nbSticks, baseWeight):
        # Si l'identifiant du neurone actuel est différent du nombre de sticks
        # restant alors nb prend maxDist*2 + 1.
        if self.index != nbSticks: nb = maxDist*2 + 1
        # Sinon, si l'identifiant du neurone actuel est égal au nombre de sticks
        # restant, alors nb prend maxDist + 1. 
        else: nb = maxDist + 1
        
        # Ensuite, on boucle de 1 à nb non inclu
        for i in range(1, nb):
            # On récupère le neurone du réseau qui se trouve à l'index i-1
            neuron = self.network.getNeuron(self.index-i)
            # Si neuron n'est pas nul, alors on initialise le poids du neurone 
            # à baseWeight
            if neuron != None: self.connections[neuron] = baseWeight
            
    def chooseConnectedNeuron(self,shift):
        neuron = None
        # TODO méthode qui retourne un neurone connecté au neurone actuel en fonction du 'shift' (cf. CPUPlayer).
        # On devra utiliser la méthode self.weighted_choice pour choisir au hasard dans une liste de connexions disponibles en fonction de leurs poids
        return neuron

    def testNeuron(self,inValue):
        return inValue - self.index <= 3 and inValue - self.index >= 1

    def recompenseConnection(self,neuron):
        # TODO récompenser la connexion entre le neurone actuel et 'neuron'
        pass

    def printConnections(self):
        print("Connections of ", self.asString() + ":")
        for neuron in self.connections:
            print(neuron.asString(),self.connections[neuron])

    def asString(self):
        return "N"+str(self.index)

    def weighted_choice(self,connections):
       total = sum(w for c, w in connections.items())
       r = random.uniform(0, total)
       upto = 0
       for c, w in connections.items():
          if upto + w >= r: return c
          upto += w
        


        


