tableau = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
#définition des index de jeu#

def Aire(tableau):
    print('┌-┬-┬-┐')
    print('│' + tableau['7'] + '│' + tableau['8'] + '│' + tableau['9'] + '│')
    print('├-┼-┼-┤')
    print('│' + tableau['4'] + '│' + tableau['5'] + '│' + tableau['6'] + '│')
    print('├-┼-┼-┤')
    print('│' + tableau['1'] + '│' + tableau['2'] + '│' + tableau['3'] + '│')
    print('└-┴-┴-┘')
#affichage du tableau#

def Morpion():
    tour = 'X'
    J = 'Joueur 1'
    compte = 0

    for i in range(10):
        Aire(tableau)
        print("C'est au tour du "+J+". Placer en quelle position?")

        move = input()

        if tableau[move] == ' ':
            tableau[move] = tour
            compte += 1
        else:
            print("Cette position est déjà prise.\nPlacer en quelle position?")
            continue

# Maintenant, vérification de victoire à chaque tour à partir du 5ième.#
        if compte >= 5:
            if tableau['7'] == tableau['8'] == tableau['9'] != ' ': #Ligne supérieur#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break
            elif tableau['4'] == tableau['5'] == tableau['6'] != ' ': #Ligne intermédiaire#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break
            elif tableau['1'] == tableau['2'] == tableau['3'] != ' ': #Ligne inférieur#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break
            elif tableau['1'] == tableau['4'] == tableau['7'] != ' ': #Ligne gauche#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break
            elif tableau['2'] == tableau['5'] == tableau['8'] != ' ': #Ligne milieu#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break
            elif tableau['3'] == tableau['6'] == tableau['9'] != ' ': #Ligne droite#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break
            elif tableau['7'] == tableau['5'] == tableau['3'] != ' ': #diagonale \#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break
            elif tableau['1'] == tableau['5'] == tableau['9'] != ' ': #diagonale /#
                Aire(tableau)
                print("\nPartie Terminée.\n")
                print(" **** " +J+ " à gagné. ****")
                break

        # Si ni le joueur 1 ou 2 ne gagne alors c'est une égalité.#
        if compte == 9:
            print("\nPartie Terminée.\n")
            print("C'est une égalité!!")

        # Changement de joueur à chaque tour.#
        if tour =='X':
            tour = 'O'
            J = 'Joueur 2'
        else:
            tour = 'X'
            J = 'Joueur 1'

Morpion()