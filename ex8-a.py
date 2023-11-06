import pandas as pd

# Remplacez 'chemin/vers/votre/fichier.csv' par le chemin réel de votre fichier CSV
chemin_fichier_csv = 'clients.csv'

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv(chemin_fichier_csv)

# Afficher les cinq premières lignes du DataFrame
print(df.head())
