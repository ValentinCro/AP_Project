# Projet d'apprentissage

## Contributeurs

* Valentin Crochemore
* Yoann Fleury

## Rapport

### Partie 5.3

En mode `easy` l'IA fait un tirage aléatoire entre 1 et 3 quelque soit le nombre
de baton restant. Donc ses tirages sont des erreurs évidentes.

### Partie 6.1

Avec la difficulté `medium` on ne parle pas encore d'apprentissage car tout est 
en dur dans le code. Il n'y a aucune progression de l'intelligence artificielle
dans le cas de `medium`. On ne devrait d'ailleurs pas parler d'intelligence 
artificielle dans ce cas.

### Partie 7

En jouant contre l'ordinateur avec la difficulté `hard`, on gagne quand même 
car ce dernier n'a pas appris à jouer correctement.

### Partie 8

Cette méthode s'appelle l'apprentissage.

On constate qu'un chemin se dégage des autres. Et qu'un des deux joueurs prends
clairement l'avantage sur l'autre.

La différence entre les deux joueurs est flagrante car en mode `hard` contre 
`hard`, vers la fin le premier joueur qui commence gagne quasiment tout le temps.

* En mode `easy` contre `easy`, c'est du 50% de victoires pour chaque.
* En mode `easy` contre `medium`, c'est clairement `medium` qui gagne avec un 
ratio de 85% de victoire.
* En mode `medium` contre `hard`, c'est clairement `hard` qui prend le dessus 
après plusieurs victoires et termine avec un ratio de 80% de victoires.
* En mode `easy` contre `hard`, c'est évidemment `hard` qui prend le dessus avec
un ratio de 90% de victoires.
* En mode `medium` contre `medium`, c'est un ratio de 50/50.

### Partie 9 : Jeu final

C'est impossible de gagner car l'ordinateur connait maintenant le chemin
menant à la victoire. Dès que l'on tire des batons, il a un coup d'avance sur 
nous et jouera toujours de façon à laisser 4 + 1 batons, ce qui nous cause une 
cuisante défaite à tous les coups.

### Partie 10 : Evaluation

Pour effectuer le calcul de taux d'erreur, nous avons mis en place un algorithme 
qui effectue 1 000 000 parties avec toujours la même intelligence artificielle 
qui commence. Sur ces 1 000 000 parties, l'intelligence artificielle ne gagne 
que 823 447 parties. On aurait pu s'attendre à que des victoires de la part 
de l'intelligence artificielle qui commence.