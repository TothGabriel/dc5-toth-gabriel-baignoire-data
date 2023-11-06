import random
import string

def generer_nom_aleatoire(longueur):
    return ''.join(random.choice(string.ascii_letters) for _ in range(longueur))

def generer_email_aleatoire(nom):
    domaines = ["example.com", "mail.com", "test.org", "fake.co"]
    return f"{nom.lower()}@{random.choice(domaines)}"

def generer_montant_depense():
    return round(random.uniform(100, 5000), 2)

# Créer une liste de 50 clients
liste_clients = []
for _ in range(50):
    nom = generer_nom_aleatoire(10)
    email = generer_email_aleatoire(nom)
    montant_depense = generer_montant_depense()
    client = {
        "nom": nom,
        "email": email,
        "montant dépensé": montant_depense
    }
    liste_clients.append(client)

# Afficher la liste des clients
for client in liste_clients:
    print(client)



clients = [
    {'nom': 'XozovzwqBr', 'email': 'xozovzwqbr@mail.com', 'montant dépensé': 3870.48},
    {'nom': 'huTudsDxio', 'email': 'hutudsdxio@example.com', 'montant dépensé': 772.97},
    {'nom': 'PwPmdqerzv', 'email': 'pwpmdqerzv@mail.com', 'montant dépensé': 1607.66},
    {'nom': 'hECSMbTbwT', 'email': 'hecsmbtbwt@mail.com', 'montant dépensé': 1764.75},
    {'nom': 'rYonJXCYdR', 'email': 'ryonjxcydr@test.org', 'montant dépensé': 3357.53},
    {'nom': 'THBaJJRdDM', 'email': 'thbajjrddm@mail.com', 'montant dépensé': 550.43},
    {'nom': 'fPBCnIqGIs', 'email': 'fpbcniqgis@example.com', 'montant dépensé': 390.06},
    {'nom': 'NHiOvnAXNi', 'email': 'nhiovnaxni@test.org', 'montant dépensé': 3177.7},
    {'nom': 'VWydQUeJeh', 'email': 'vwydquejeh@test.org', 'montant dépensé': 2143.03},
    {'nom': 'kJMRkZCwol', 'email': 'kjmrkzcwol@example.com', 'montant dépensé': 2074.87},
    {'nom': 'tajdZfxgJT', 'email': 'tajdzfxgjt@fake.co', 'montant dépensé': 4974.84},
    {'nom': 'AhRSPbNltb', 'email': 'ahrspbnltb@test.org', 'montant dépensé': 2910.05},
    {'nom': 'QEOgAdeCcW', 'email': 'qeogadeccw@example.com', 'montant dépensé': 4498.6},
    {'nom': 'woMLwvGSxl', 'email': 'womlwvgsxl@test.org', 'montant dépensé': 3622.1},
    {'nom': 'bZnNYHKdmI', 'email': 'bznnyhkdmi@fake.co', 'montant dépensé': 3607.41},
    {'nom': 'CaZfbLPSef', 'email': 'cazfblpsef@fake.co', 'montant dépensé': 4630.23},
    {'nom': 'ibhJTwTCof', 'email': 'ibhjtwtcof@fake.co', 'montant dépensé': 4334.45},
    {'nom': 'PjnubMdTkN', 'email': 'pjnubmdtkn@example.com', 'montant dépensé': 4220.8},
    {'nom': 'vKlWlmOfTp', 'email': 'vklwlmoftp@fake.co', 'montant dépensé': 1004.79},
    {'nom': 'rtHgOzoipv', 'email': 'rthgozoipv@example.com', 'montant dépensé': 3896.14},
    {'nom': 'jjFgNWJaAI', 'email': 'jjfgnwjaai@example.com', 'montant dépensé': 4965.75},
    {'nom': 'LHmukHxMbI', 'email': 'lhmukhxmbi@test.org', 'montant dépensé': 993.62},
    {'nom': 'LfeNsPeBMq', 'email': 'lfenspebmq@test.org', 'montant dépensé': 4455.68},
    {'nom': 'LicPzrZbwo', 'email': 'licpzrzbwo@example.com', 'montant dépensé': 1770.71},
    {'nom': 'oAmrrzbjzZ', 'email': 'oamrrzbjzz@test.org', 'montant dépensé': 864.41},
    {'nom': 'SwydzGAIeS', 'email': 'swydzgaies@mail.com', 'montant dépensé': 2828.25},
    {'nom': 'xsRndBwpFc', 'email': 'xsrndbwpfc@test.org', 'montant dépensé': 4381.61},
    {'nom': 'jvbJwQsfxg', 'email': 'jvbjwqsfxg@example.com', 'montant dépensé': 1459.95},
    {'nom': 'qRQjebJZwu', 'email': 'qrqjebjzwu@fake.co', 'montant dépensé': 1312.73},
    {'nom': 'ZYXacDroMh', 'email': 'zyxacdromh@example.com', 'montant dépensé': 506.34},
    {'nom': 'BlwbvzpQWm', 'email': 'blwbvzpqwm@fake.co', 'montant dépensé': 4602.68},
    {'nom': 'HuiVmcYcmZ', 'email': 'huivmcycmz@example.com', 'montant dépensé': 3692.87},
    {'nom': 'LIwNzFVwss', 'email': 'liwnzfvwss@example.com', 'montant dépensé': 4939.08},
    {'nom': 'MNAOkUDYwV', 'email': 'mnaokudywv@mail.com', 'montant dépensé': 147.82},
    {'nom': 'UFmMtwXxoC', 'email': 'ufmmtwxxoc@example.com', 'montant dépensé': 2886.26},
    {'nom': 'TvIFUxMFvR', 'email': 'tvifuxmfvr@example.com', 'montant dépensé': 686.48},
    {'nom': 'TzlSDTeLzE', 'email': 'tzlsdtelze@mail.com', 'montant dépensé': 983.79},
    {'nom': 'OMNGzADXNd', 'email': 'omngzadxnd@example.com', 'montant dépensé': 4514.39},
    {'nom': 'ydxnWwJaym', 'email': 'ydxnwwjaym@test.org', 'montant dépensé': 2638.27},
    {'nom': 'GPlZiTkdNN', 'email': 'gplzitkdnn@fake.co', 'montant dépensé': 2606.56},
    {'nom': 'iRlNyCRMBJ', 'email': 'irlnycrmbj@mail.com', 'montant dépensé': 3756.92},
    {'nom': 'gVcLaiCJwR', 'email': 'gvclaicjwr@mail.com', 'montant dépensé': 3946.98},
    {'nom': 'aaEfHFoMtO', 'email': 'aaefhfomto@test.org', 'montant dépensé': 3266.88},
    {'nom': 'aODKDStKKT', 'email': 'aodkdstkkt@mail.com', 'montant dépensé': 4188.11},
    {'nom': 'nLsNIboJSs', 'email': 'nlsnibojss@test.org', 'montant dépensé': 956.81},
    {'nom': 'xfAGFOcMaw', 'email': 'xfagfocmaw@example.com', 'montant dépensé': 2309.41},
    {'nom': 'ssfFFNOsiO', 'email': 'ssfffnosio@test.org', 'montant dépensé': 4636.82},
    {'nom': 'guHVGfiSzA', 'email': 'guhvgfisza@mail.com', 'montant dépensé': 1213.47},
    {'nom': 'bKnZKcCvZd', 'email': 'bknzkccvzd@fake.co', 'montant dépensé': 3414.71},
    {'nom': 'qzDjZCEPRJ', 'email': 'qzdjzceprj@fake.co', 'montant dépensé': 4269.0}
]


