# Projet « Puissance 4 »

**Spécification des fonctions :**

def grille_vide():
'''
Fonction grille_vide():
La fonction construit un tableau à deux dimensions de taille 6 x 7 : 6 lignes et 7 colonnes.
Chaque case contient la valeur 0.
    La fonction ne prend pas d'argument.
    La fonction renvoie le tableau.
'''

def affiche(gril):
'''
Fonction affiche(gril): affiche une grille de 6 lignes sur 7 colonnes.
La fonction prend en argument un tableau de taille 6 x 7.
Une ligne est notée lig et prend une valeur entre 0 et 5, la ligne 0 est située en bas.
Une colonne est notée col et prend une valeur entre 0 et 6, la colonne 0 est située à gauche.
Dans la grille:
    la valeur 0 représente une case vide, représentée par un.
    la valeur 1 représente un pion du joueur 1, représenté par un x.
    la valeur 2 représente un pion du joueur 2, représenté par un 0.
'''

def coup_possible(gril, col):
'''
Fonction coup_possible(gril, col) :
Détermine s’il est possible de jouer dans la colonne col.
Prend en argument la grille, tableau de 5x6, avec la position des pions des joueurs et un entier, le numéro de colonne entre 0 et 6.
Renvoie True s’il est possible de jouer dans la colonne col, False sinon.
Il est possible de jouer dans la colonne col, si il existe une case avec la valeur 0 dans cette colonne.
'''

def jouer(gril, j, col):
'''
Fonction jouer(gril, j, col):
Fonction qui joue un coup du joueur j dans la colonne col de la grille.
Arguments:
    gril est la grille de 5 x 6 avec les pions des joueurs.
    j est un entier qui a la valeur 1 ou 2 suivant le joueur.
    col est un entier entre 0 et 6 et désigne une colonne non pleine de la grille.
Si j vaut 1 la première case vide de la colonne col prendra la valeur 1
Si j vaut 2 la première case vide de la colonne col prendra la valeur 2
'''

def horiz (gril, j, lig):
'''
Fonction horiz(gril, j, lig):
Détermine si il y a un alignement horizontal de 4 pions du joueur j à partir de la ligne (lig).
arguments:
    gril la grille avec les pions.
    j le joueur, un entier avec la valeur 1 ou 2.
    lig la ligne, un entier avec la valeur entre 0 et 5.
    col la colonne, un entier avec la valeur entre 0 et 6.
Renvoie True si c'est le cas.
'''

def vert(gril, j, lig, col):
'''
Fonction vert(gril, j, lig, col):
Détermine si il y a un alignement vertical de 4 pions du joueur j à partir de la colonne (col).
arguments:
    grill la grille avec les pions.
    j le joueur, un entier avec la valeur 1 ou 2.
    lig la ligne, un entier avec la valeur entre 0 et 5.
    col la colonne, un entier avec la valeur entre 0 et 6.
Renvoie True si c'est le cas.
'''

def diag_haut(gril, j, lig, col):
'''
Fonction diag_haut(gril, j, lig, col):
Détermine si il y a un alignement diagonal vers le haut de 4 pions du joueur j à partir de la case (lig,col).
Arguments:
gril la grille avec les pions.
    j le joueur, un entier avec la valeur 1 ou 2.
    lig la ligne, un entier avec la valeur entre 0 et 5.
    col la colonne, un entier avec la valeur entre 0 et 6.
Renvoie True si c'est le cas, False sinon.
'''

def diag_bas(gril, j, lig, col):
'''
Fonction diag_bas(gril, j, lig, col):
Détermine si il y a un alignement diagonal vers le haut de 4 pions du joueur j à partir de la case (lig,col).
Arguments:
    gril la grille avec les pions.
    j le joueur, un entier avec la valeur 1 ou 2.
    lig la ligne, un entier avec la valeur entre 0 et 5.
    col la colonne, un entier avec la valeur entre 0 et 6.
Renvoie True si c'est le cas, False sinon.
'''

def victoire(gril, j):
'''
fonction victoire(gril, j):
Renvoie un booléen True si le joueur j a gagné, False sinon.
Fait appel aux fonctions horiz(), vert(), diag_haut() et diag_bas()
'''

def match_nul(gril):
'''
Fonction match_nul(gril):
Renvoie True si la partie est nulle, c'est à dire si la ligne du haut est remplie,False sinon.
'''

def coup_aleatoire(gril,j):
'''
Fonction coup_aleatoire(gril,j):
Joue un coup aléatoire pour le joueur j.
On suppose la grille non pleine, condition indispensable pour ne pas se trouver dans une boucle infinie !
'''
