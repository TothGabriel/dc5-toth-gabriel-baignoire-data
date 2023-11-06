def factoriel_iterative(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

# Test de la fonction
print(factoriel_iterative(5))  # Devrait retourner 120
print(factoriel_iterative(7))  # Devrait retourner 5040
