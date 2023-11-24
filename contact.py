# Initialiser un dictionnaire vide pour stocker les contacts
contacts = {}

# Fonction pour ajouter un contact
def ajouter_contact(nom, numero):
    contacts[nom] = numero
    print(f"Contact {nom} ajouté avec succès.")

# Fonction pour supprimer un contact
def supprimer_contact(nom):
    if nom in contacts:
        del contacts[nom]
        print(f"Contact {nom} supprimé avec succès.")
    else:
        print(f"Le contact {nom} n'existe pas.")

# Fonction pour rechercher un contact
def rechercher_contact(nom):
    if nom in contacts:
        print(f"Nom: {nom}, Numéro de téléphone: {contacts[nom]}")
    else:
        print(f"Le contact {nom} n'existe pas.")

# Boucle principale du programme
while True:
    print("\n1. Ajouter un contact")
    print("2. Supprimer un contact")
    print("3. Rechercher un contact")
    print("4. Quitter")

    choix = input("Choisissez une option (1/2/3/4) : ")

    if choix == "1":
        nom = input("Entrez le nom du contact : ")
        numero = input("Entrez le numéro de téléphone : ")
        ajouter_contact(nom, numero)

    elif choix == "2":
        nom = input("Entrez le nom du contact que vous souhaitez supprimer : ")
        supprimer_contact(nom)

    elif choix == "3":
        nom = input("Entrez le nom du contact que vous souhaitez rechercher : ")
        rechercher_contact(nom)

    elif choix == "4":
        print("Programme terminé.")
        break

    else:
        print("Option non valide. Veuillez choisir une option valide.")