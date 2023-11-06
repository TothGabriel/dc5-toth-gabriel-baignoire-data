# Demander à l'utilisateur d'entrer le coût de la campagne
cout_campagne = float(input("Entrez le coût de la campagne (EUR): "))

# Demander à l'utilisateur d'entrer le revenu généré par la campagne
revenu_genere = float(input("Entrez le revenu généré par la campagne (EUR): "))

# Comparer le coût et le revenu pour déterminer la rentabilité
if revenu_genere > cout_campagne:
    profit = revenu_genere - cout_campagne
    print(f"La campagne a été rentable. Le profit est de {profit:.2f} EUR.")
elif revenu_genere == cout_campagne:
    print("La campagne a atteint le seuil de rentabilité mais n'a pas généré de profit.")
else:
    perte = cout_campagne - revenu_genere
    print(f"La campagne n'a pas été rentable. La perte est de {perte:.2f} EUR.")
