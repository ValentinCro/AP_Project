#LE main

from Game import *
from Player import *

nbSticks = 15

vous = HumanPlayer("Le plus beau")
ordi = CPUPlayer("Le mechant ordi", "easy", nbSticks)
game = Game(nbSticks)
game.start(vous, ordi, True)