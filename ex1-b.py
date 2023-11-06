# Demander à l'utilisateur de saisir une phrase
phrase = input("Veuillez saisir une phrase : ")

# Afficher la phrase en majuscules
print("Phrase en majuscules:", phrase.upper())

# Afficher la phrase en minuscules
print("Phrase en minuscules:", phrase.lower())

# Calculer et afficher le nombre de mots
nombre_de_mots = len(phrase.split())
print("Nombre de mots dans la phrase:", nombre_de_mots)
