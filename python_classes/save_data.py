# Script main permettant de lancer le jeu.

from Game import Game
from Player import *
import pickle

NB_STICKS = 15

cpu1 = CPUPlayer("CPU_1", "hard", NB_STICKS)
cpu2 = CPUPlayer("CPU_2", "hard", NB_STICKS)
for i in range(1, 20000):
    Game(NB_STICKS).start(cpu1, cpu2, False)
    

with open("data",'wb') as output: pickle.dump(cpu1.getNeuronNetwork(), output, pickle.HIGHEST_PROTOCOL)