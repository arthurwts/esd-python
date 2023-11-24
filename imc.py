def calcul_imc_et_categorie(taille, poids):
    """
    Calcule l'Indice de Masse Corporelle (IMC) et détermine la catégorie d'IMC.

    :param taille: Taille en mètres.
    :param poids: Poids en kilogrammes.
    :return: Valeur de l'IMC et catégorie d'IMC.
    """
    imc = poids / (taille ** 2)

    # Déterminer la catégorie d'IMC
    if imc < 18.5:
        categorie = "Insuffisance pondérale"
    elif 18.5 <= imc < 25:
        categorie = "Poids normal"
    elif 25 <= imc < 30:
        categorie = "Surpoids"
    elif 30 <= imc < 35:
        categorie = "Obésité modérée"
    elif 35 <= imc < 40:
        categorie = "Obésité sévère"
    else:
        categorie = "Obésité très sévère (morbidité)"

    return imc, categorie

# Exemple d'utilisation
taille_utilisateur = 1.85  # en mètres
poids_utilisateur = 70  # en kilogrammes

imc_utilisateur, categorie_imc_utilisateur = calcul_imc_et_categorie(taille_utilisateur, poids_utilisateur)

print("Taille:" , taille_utilisateur, "m, Poids:", poids_utilisateur, "kg")
print("Indice de Masse Corporelle (IMC):" , imc_utilisateur)
print("Catégorie d'IMC:" , categorie_imc_utilisateur)
