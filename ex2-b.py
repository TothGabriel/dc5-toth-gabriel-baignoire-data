# Liste de 10 nombres
nombres = [23, 1, 45, 34, 87, 56, 12, 8, 30, 25]

# Initialiser max et min avec le premier élément de la liste
max_nombre = nombres[0]
min_nombre = nombres[0]

# Initialiser la somme pour calculer la moyenne
somme_nombres = 0

# Boucle pour trouver le max, le min et la somme
for nombre in nombres:
    if nombre > max_nombre:
        max_nombre = nombre
    if nombre < min_nombre:
        min_nombre = nombre
    somme_nombres += nombre

# Calcul de la moyenne
moyenne_nombres = somme_nombres / len(nombres)

# Affichage des résultats
print("Maximum:", max_nombre)
print("Minimum:", min_nombre)
print("Moyenne:", moyenne_nombres)
