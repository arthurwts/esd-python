def tri_bulles(liste):

    # Créer une copie de la liste pour éviter de modifier la liste d'origine
    liste_copie = liste.copy()
    n = len(liste_copie)

    # Parcourir tous les éléments de la liste
    for i in range(n):
        # Le dernier i éléments sont déjà triés, pas besoin de les vérifier
        for j in range(0, n - i - 1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if liste_copie[j] > liste_copie[j + 1]:
                liste_copie[j], liste_copie[j + 1] = liste_copie[j + 1], liste_copie[j]

    return liste_copie

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
liste_triee = tri_bulles(ma_liste)

print("Liste d'origine :", ma_liste)
print("Liste triée :", liste_triee)
