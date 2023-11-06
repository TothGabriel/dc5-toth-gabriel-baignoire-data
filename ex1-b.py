# Demander à l'utilisateur de saisir une phrase
phrase = input("Veuillez saisir une phrase : ")

# Convertir la phrase en majuscules sans utiliser .upper()
phrase_majuscules = ''
for caractere in phrase:
    if 'a' <= caractere <= 'z':  # Vérifier si c'est une lettre minuscule
        phrase_majuscules += chr(ord(caractere) - 32)  # Convertir en majuscule
    else:
        phrase_majuscules += caractere

# Convertir la phrase en minuscules sans utiliser .lower()
phrase_minuscules = ''
for caractere in phrase:
    if 'A' <= caractere <= 'Z':  # Vérifier si c'est une lettre majuscule
        phrase_minuscules += chr(ord(caractere) + 32)  # Convertir en minuscule
    else:
        phrase_minuscules += caractere

# Compter le nombre de mots sans utiliser .split()
nombre_de_mots = 0
dans_mot = False
for caractere in phrase:
    if caractere.isalpha():  # Vérifier si le caractère est une lettre
        if not dans_mot:
            nombre_de_mots += 1
            dans_mot = True
    else:
        dans_mot = False

# Afficher les résultats
print("Phrase en majuscules:", phrase_majuscules)
print("Phrase en minuscules:", phrase_minuscules)
print("Nombre de mots dans la phrase:", nombre_de_mots)
