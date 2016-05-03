# Script main permettant de lancer le jeu.

from Game import Game
from Player import *

NB_STICKS = 15

human = HumanPlayer("Humain")
cpu = CPUPlayer("CPU", "hard", NB_STICKS)
Game(NB_STICKS).start(human, cpu, True)
