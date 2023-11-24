def trier_et_afficher_liste(liste):
    
    # Ajouter des éléments à la liste
    liste.append(7)
    liste.extend([4, 6])

    # Afficher la liste avant le tri
    print("Liste avant le tri :", liste)

    # Trier la liste
    liste.sort()

    # Afficher la liste après le tri
    print("Liste après le tri :", liste)

# Exemple d'utilisation de la fonction
ma_liste = [5, 2, 8, 1, 3]

def afficher_informations_personne(personne):
    # Exemple d'utilisation de la fonction
    personne = {
        "nom": "Arthur",
        "age": 20,
        "adresse": "7 Rue du Pingouin",
        "email": "mail@mail.com"
    }
    # Afficher les informations sur la personne
    print("Informations sur la personne :")
    print("Nom :", personne["nom"])
    print("Âge :", personne["age"])
    print("Adresse :", personne["adresse"])
    print("Email :", personne["email"])

def operations_ensembles(ensemble1, ensemble2):
   
    # Afficher les ensembles
    print("Ensemble 1 :", ensemble1)
    print("Ensemble 2 :", ensemble2)

    # Union des ensembles
    union_ensembles = ensemble1.union(ensemble2)
    print("Union :", union_ensembles)

    # Intersection des ensembles
    intersection_ensembles = ensemble1.intersection(ensemble2)
    print("Intersection :", intersection_ensembles)

# Exemple d'utilisation de la fonction
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}