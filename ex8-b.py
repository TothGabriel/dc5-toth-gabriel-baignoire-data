def compter_mots(texte):
    nombre_mots = 0
    dans_mot = False
    for caractere in texte:
        if caractere.isalpha():  # Vérifie si le caractère est une lettre
            if not dans_mot:
                nombre_mots += 1  # Commence un nouveau mot
                dans_mot = True
        else:
            dans_mot = False  # Fin d'un mot
    return nombre_mots

# Lire le fichier texte
chemin_fichier_lecture = 'texte.txt'
try:
    with open(chemin_fichier_lecture, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        nombre_mots = compter_mots(contenu)
except FileNotFoundError:
    print(f"Le fichier {chemin_fichier_lecture} n'a pas été trouvé.")
    nombre_mots = 0

# Écrire le résultat dans un autre fichier
chemin_fichier_ecriture = 'resultat.txt'
with open(chemin_fichier_ecriture, 'w', encoding='utf-8') as fichier:
    fichier.write(f"Nombre de mots dans le fichier : {nombre_mots}\n")

print(f"Le nombre de mots a été écrit dans {chemin_fichier_ecriture}.")
