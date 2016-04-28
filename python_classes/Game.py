# Inutile de modifier cette classe normalement

class Game:

    def __init__(self,nbSticks):
        self.nbSticks = nbSticks

    def start(self,player1,player2,verbose):
        # Verbose active ou désactive les print
        if verbose: print("New game")
        sticks = self.nbSticks
        # On met le joueur courrant égale au joueur 1
        currp = player1
        # Tant qu'il reste des batons
        while sticks>0:
            if verbose: print("Remaining sticks:",sticks)
            # Le joueur choisi combien de baton il retire
            n = currp.play(sticks)
            # On affiche un message si le joueur retire plus ou moins de baton que
            # La limite
            if n<1 or n>3: print("Error")
            if verbose: print(currp.getName(),"takes",n)
            # On retire les batons
            sticks-=n
            # On change le joueur courant
            if currp==player1: currp = player2
            else: currp = player1
        if verbose: print(currp.getName(),"wins!")
        # Une fois la boucle fini la partie est fini
        # Si le joueur courant est le joueur 1 c'est que 
        # c'est le joueur 2 qui à retire le dernier baton (resp)
        if player1==currp:
            player1.addWin()
            player2.addLoss()
        else:
            player1.addLoss()
            player2.addWin()
