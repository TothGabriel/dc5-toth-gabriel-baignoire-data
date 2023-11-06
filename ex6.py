from ex5 import clients

# Parcourir la liste des clients et afficher ceux qui ont dépensé plus de 100€
for client in clients:
    if client['montant dépensé'] > 100:
        print(f"{client['nom']} a dépensé {client['montant dépensé']}€")
