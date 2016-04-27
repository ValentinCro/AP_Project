# Script main permettant de lancer le jeu.

from python_classes.Game import Game
from python_classes.Player import *

nbSticks = 15

human = HumanPlayer("Humain")
cpu = CPUPlayer("CPU", "medium", nbSticks)
Game(nbSticks).start(human, cpu, True)
