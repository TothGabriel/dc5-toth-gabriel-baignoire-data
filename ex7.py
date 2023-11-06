from ex5 import clients

def calculer_montant_total(clients):
    total = 0
    for client in clients:
        total += client['montant dépensé']
    return total



# Appel de la fonction et affichage du résultat
montant_total = calculer_montant_total(clients)
print(f"Le montant total dépensé par tous les clients est de {montant_total}€")
