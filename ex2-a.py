# Liste des dépenses marketing mensuelles
depenses_mensuelles = [1200, 1100, 1300, 1000, 1050, 1100, 1200, 1250, 1300, 1400, 1350, 1450]

# Calcul des dépenses totales de l'année
depenses_annuelles = 0
for depense in depenses_mensuelles:
    depenses_annuelles += depense

# Affichage des dépenses totales
print("Les dépenses marketing totales de l'année sont :", depenses_annuelles, "euros.")
