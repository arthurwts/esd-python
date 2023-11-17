def sommenombres():
    # Demander à l'utilisateur un nombre entier N
    N = int(input("Entrez un nombre entier N :"))

    # Initialiser la somme
    somme = 0

    # Calculer la somme des nombres de 1 à N avec une boucle for
    for i in range(1, N + 1):
        somme += i

    # Afficher le résultat
    print("La somme des nombres de 1 à", N, "est :", somme)


# Appeler la fonction sommenombres
sommenombres()

def tableM():
    # Demander à l'utilisateur un nombre entier N
    N = int(input("Entrez un nombre entier N :"))

    # Afficher la table de multiplication de N de 1 à 10 avec une boucle for
    print("Table de multiplication de", N, ":")
    for i in range(1, 11):
        resultat = N * i
        print(N, "x", i, "=", resultat)

# Appeler la fonction tableM
tableM()

def pairouimpair():
    # Utiliser une boucle for pour afficher les nombres de 1 à 10
    for i in range(1, 11):
        # Vérifier si le nombre est pair ou impair
        if i % 2 == 0:
            print(i, "est un nombre pair.")
        else:
            print(i, "est un nombre impair.")

# Appeler la fonction pairouimpair
pairouimpair()

def factorielle():
    # Demander à l'utilisateur un nombre entier N
    N = int(input("Entrez un nombre entier N :"))

    # Initialiser la variable pour stocker la factorielle
    factorielle = 1

    # Calculer la factorielle de N avec une boucle for
    for i in range(1, N + 1):
        factorielle *= i

    # Afficher le résultat
    print("La factorielle de", N, "est :", factorielle)

# Appeler la fonction factorielle
factorielle()

def est_palindrome():
    import unicodedata
    # Demander à l'utilisateur de saisir un mot
    mot = input("Entrez un mot : ")

    # Convertir le mot en minuscules pour éviter les différences de cas
    mot = mot.lower()

    # Supprimer les accents
    mot = ''.join(char for char in unicodedata.normalize('NFD', mot) if unicodedata.category(char) != 'Mn')

    # Supprimer la ponctuation
    mot = ''.join(char for char in mot if char.isalnum())

    # Vérifier si le mot est un palindrome
    if mot == mot[::-1]:
        print("Le mot", mot, "est un palindrome.")
    else:
        print("Le mot", mot, "n'est pas un palindrome.")

# Appeler la fonction est_palindrome
est_palindrome()

def creaCarreMagique(n):
    carre_magique = [[0] * n for t in range(n)]

    x, y = 0, n // 2
    num = 1

    while num <= n * n:
        carre_magique[x][y] = num
        num += 1
        newx, newy = (x - 1) % n, (y + 1) % n

        if carre_magique[newx][newy] == 0:
            x, y = newx, newy
        else:
            x = (x + 1) % n

    return carre_magique

def print_square(square):
    for row in square:
        print(" ".join(map(str, row)))

# Exemple d'utilisation pour un carré magique d'ordre 3
n = 3
carre_magique = creaCarreMagique(n)
print_square(carre_magique)