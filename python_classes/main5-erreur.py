# Script main permettant de lancer le jeu.

from Game import Game
from Player import *
import pickle
import os.path

NB_STICKS = 15

# Permet de charger le NeuronNetwork
if os.path.isfile('data') :
    with open('data', 'rb') as inp: network = pickle.load(inp)
    netw = network
    
cpu1 = CPUPlayer("Ordinateur1", 'hard', NB_STICKS)
cpu2 = CPUPlayer("Ordinateur2", 'hard', NB_STICKS)

with open('data', 'rb') as inp: ns = pickle.load(inp)
cpu1.setNeuronNetwork(ns)
cpu2.setNeuronNetwork(ns)

for i in range(1, 1000000) :
    Game(NB_STICKS).start(cpu1, cpu2, False)
    print(i)
    
print(cpu1.getNbWin())