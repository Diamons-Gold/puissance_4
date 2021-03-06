def grille_vide():
    '''
    Fonction grille_vide():
    La fonction construit un tableau à deux dimensions de taille 6 x 7 : 6 lignes et 7 colonnes.
    Chaque case contient la valeur 0.
        La fonction ne prend pas d'argument.
        La fonction renvoie le tableau.
    '''

    return [[0 for i in range(7)] for i in range(6)]

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

    aff = [[]]*6

    for i in range(6):
        aff[i] = '|'.join([str(j) for j in gril[i]]).replace('0','.').replace('1','X').replace('2','0')

    print(
        '  0 1 2 3 4 5 6 \n'
        '  -------------\n'
        '5', aff[5],'\n'
        '4', aff[4],'\n'
        '3', aff[3],'\n'
        '2', aff[2],'\n'
        '1', aff[1],'\n'
        '0', aff[0],'\n'
        '  -------------')

def coup_possible(gril, col):
    '''
    Fonction coup_possible(gril, col) :
    Détermine s’il est possible de jouer dans la colonne col.
    Prend en argument la grille, tableau de 5x6, avec la position des pions des joueurs et un entier, le numéro de colonne entre 0 et 6.
    Renvoie True s’il est possible de jouer dans la colonne col, False sinon.
    Il est possible de jouer dans la colonne col, si il existe une case avec la valeur 0 dans cette colonne.
    '''
    
    if 0 in [gril[i][col] for i in range(6)]:
        return True
    return False

def jouer(gril, j, col):
    '''
    Fonction jouer(gril, j, col):
    Fonction qui joue un coup du joueur j dans la colonne col de la grille.
    Arguments:
    gril est la grille de 5 x 6 avec les pions des joueurs
        j est un entier qui a la valeur 1 ou 2 suivant le joueur.
        col est un entier entre 0 et 6 et désigne une colonne non pleine de la grille.
    Si j vaut 1 la première case vide de la colonne col prendra la valeur 1
    Si j vaut 2 la première case vide de la colonne col prendra la valeur 2
    '''

    if coup_possible(gril, col):
        for i in range(6):
            if gril[i][col] == 0:
                gril[i][col] = j
                affiche(gril)
                return

def horiz(gril, j, lig): # del col
    '''
    Fonction horiz(gril, j, lig, col):
    Détermine si il y a un alignement horizontal de 4 pions du joueur j
    à partir de la case (lig,col).
    arguments: 
        gril la grille avec les pions.
        j le joueur, un entier avec la valeur 1 ou 2
        lig la ligne, un entier avec la valeur entre 0 et 5
    Renvoie True si c'est le cas.
    '''

    if j in gril[lig]:
        comp = 0
        for i in gril[lig]:
            if j == i:
                comp += 1
            else:
                comp = 0
            if comp >= 4:
                return True
    return False

def vert(gril, j, col): # del lig
    '''
    Fonction vert(gril, j, lig, col):
    Détermine si il y a un alignement vertical de 4 pions du joueur j
    à partir de la case (lig,col).
    arguments:
        grill la grille avec les pions.
        j le joueur, un entier avec la valeur 1 ou 2
        col la colonne, un entier avec la valeur entre 0 et 6
    Renvoie True si c'est le cas.
    '''

    vert = [gril[i][col] for i in range(6)]

    print(vert)

    if j in vert:
        comp = 0
        for i in vert:
            if j == i:
                comp += 1
            else:
                comp = 0
            if comp >= 4:
                return True
    return False

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
    
    diag = []
    d = col
    h = 5 - lig

    if d > h :
        d -= d - h 
    elif h > d :
        h -= h - d 

    while not(lig + h == -1) and not(col - d == 7):
        diag.append(gril[lig + h][col - d])
        d -= 1
        h -= 1

    if j in diag:
        comp = 0
        for i in diag:
            if j == i:
                comp += 1
            else:
                comp = 0
            if comp >= 4:
                return True
    return False
    
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
    
    diag = []
    d = col
    h = 5 - lig

    if d > h :
        d -= d - h 
    elif h > d :
        h -= h - d 

    while not(lig + h == -1) and not(col - d == -1):
        diag.append(gril[lig + h][col + d])
        d -= 1
        h -= 1

    if j in diag:
        comp = 0
        for i in diag:
            if j == i:
                comp += 1
            else:
                comp = 0
            if comp >= 4:
                return True
    return False

def victoire(gril, j, lig, col): # add lig, add col
    '''
    fonction victoire(gril, j):
    Renvoie un booléen True si le joueur j a gagné, False sinon.
    Fait appel aux fonctions horiz(), vert(), diag_haut() et diag_bas()
    '''

    if horiz(gril, j, lig) == True:
        return True
    elif vert(gril, j, col) == True:
        return True
    elif diag_haut(gril, j, lig, col) == True:
        return True
    elif diag_bas(gril, j, lig, col) == True:
        return True
    return False
    

def match_nul(gril):
    '''
    Fonction match_nul(gril):
    Renvoie True si la partie est nulle, c'est à dire si la ligne du haut est remplie,False sinon.
    '''

    if not(0 in [gril[i] for i in range(6)]):
        return True
    return False

from random import randint

def coup_aleatoire(gril, j):
    '''
    Fonction coup_aleatoire(gril,j):
    Joue un coup aléatoire pour le joueur j.
    On suppose la grille non pleine, condition indispensable pour ne pas se trouver dans une boucle infinie !
    '''

    test = False
    while not(test):
        col = randint(0,6)
        test = coup_possible(gril, col)

    jouer(gril, j, col)


def run():
    gril = grille_vide()
    for i in range(1,42):
        j = 2 - i%2
        col = int(input(f'Dans qu\'elle colonne voulez vous jouer joueur {j} : '))
        while col < 0 or col > 6 :
            col = int(input(f'Votre reponse est incorecte ! \n Dans qu\'elle colonne voulez vous jouer joueur {j} : '))
        jouer(gril, j, col)

run()