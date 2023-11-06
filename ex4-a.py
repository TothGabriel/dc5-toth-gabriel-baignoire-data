def convertir_ctr_en_pourcentage(clics, impressions):
    """
    Convertit le CTR en pourcentage à partir du nombre de clics et d'impressions.

    :param clics: Nombre de clics.
    :param impressions: Nombre d'impressions.
    :return: Le CTR en pourcentage.
    """
    if impressions == 0:  # Pour éviter la division par zéro
        return "Indéfini - Les impressions ne peuvent pas être zéro."
    
    ctr = (clics / impressions) * 100
    return ctr

# Test de la fonction avec plusieurs entrées
print(f"CTR: {convertir_ctr_en_pourcentage(150, 1000):.2f}%")  # Devrait retourner 15.00%
print(f"CTR: {convertir_ctr_en_pourcentage(300, 10000):.2f}%") # Devrait retourner 3.00%
print(f"CTR: {convertir_ctr_en_pourcentage(75, 500):.2f}%")    # Devrait retourner 15.00%
print(f"CTR: {convertir_ctr_en_pourcentage(0, 1000):.2f}%")    # Devrait retourner 0.00%
print(f"CTR: {convertir_ctr_en_pourcentage(250, 0)}")          # Devrait retourner "Indéfini - Les impressions ne peuvent pas être zéro."
