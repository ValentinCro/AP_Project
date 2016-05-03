# Script main permettant de lancer le jeu.

from Game import Game
from Player import *

NB_STICKS = 15

cpu1 = CPUPlayer("CPU_HUGE_LARGE_DICK", "hard", NB_STICKS)
cpu2 = CPUPlayer("CPU_LITTLE_DICK", "hard", NB_STICKS)
for i in range(1, 5001):
    Game(NB_STICKS).start(cpu1, cpu2, False)

cpu1.getNeuronNetwork().printAllConnections()