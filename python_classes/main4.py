# Script main permettant de lancer le jeu.

from Game import Game
from Player import *
from pickle import *

NB_STICKS = 15

cpu1 = CPUPlayer("CPU_1", "hard", NB_STICKS)
cpu2 = CPUPlayer("CPU_2", "hard", NB_STICKS)
for i in range(1, 5001):
    Game(NB_STICKS).start(cpu1, cpu2, False)
    Game(NB_STICKS).start(cpu2, cpu1, False)
    
with open("data",'wb') as output: dump(cpu1.getNeuronNetwork(), output, HIGHEST_PROTOCOL)
