# Script main permettant de lancer le jeu.

from Game import Game
from Player import *

NB_STICKS = 15

cpu1 = CPUPlayer("CPU_1", "medium", NB_STICKS)
cpu2 = CPUPlayer("CPU_2", "medium", NB_STICKS)
for i in range(1, 5001):
    Game(NB_STICKS).start(cpu1, cpu2, False)
    print(cpu1.getName(), ' a gagne : ' , cpu1.getNbWin())
    print(cpu2.getName(), ' a gagne : ' , cpu2.getNbWin())
