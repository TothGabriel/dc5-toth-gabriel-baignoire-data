def factoriel_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factoriel_recursive(n - 1)

# Test de la fonction
print(factoriel_recursive(5))  # Devrait retourner 120
print(factoriel_recursive(7))  # Devrait retourner 5040