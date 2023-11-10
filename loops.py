# écrire une fonction "multiplie" qui multiplie deux nombres en paramètre par additions successives. 

def multiplie(a, b):
    # Initialise le résultat à zéro
    resultat = 0

    # Utilise une boucle pour ajouter 'a' à 'resultat' 'b' fois
    for i in range(b):
        resultat += a

    return resultat

# Exemple d'utilisation de la fonction multiplie
x = int(input("Saisissez une première valeur: "))
y = int(input("Saisissez une seconde valeur: "))
produit = multiplie(x, y)
print("Le résultat de la multiplication est :", x, "*", y, "=", produit)

# Faire aussi une fonction "puissance" qui calcule les puissances par multiplication successives.

def puissance(base, exposant):
    # Initialise le résultat à 1
    resultat = 1

    # Utilise une boucle pour multiplier 'base' par lui-même 'exposant' fois
    for _ in range(exposant):
        resultat *= base

    return resultat

# Exemple d'utilisation de la fonction puissance
base = int(input("Saisissez la base: "))
exposant = int(input("Saisissez l'exposant: "))
resultat = puissance(base, exposant)
print("Le résultat du calcul de puissance est :", base, "^", exposant, "=", resultat)