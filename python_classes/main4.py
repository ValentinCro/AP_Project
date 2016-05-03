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

humanName = input('Quel est votre nom ? ')
human = HumanPlayer(humanName)

difficulty = ''
while difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard' :
    difficulty = input('Quel niveau de difficulté ? (easy, medium, hard) ')
cpu1 = CPUPlayer("Ordinateur", difficulty, NB_STICKS, netw)

if(difficulty == "hard"):
	with open('data', 'rb') as inp: ns = pickle.load(inp)
	cpu1.setNeuronNetwork(ns)

Game(NB_STICKS).start(cpu1, human, True)
