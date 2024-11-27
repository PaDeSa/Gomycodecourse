# Message de bienvenue

print("Bienvenue dans Python Pizza Deliveries!")

# Demandes à l'utilisateur
size = input("Quelle taille de pizza souhaitez-vous ? S, M, ou L: ").upper()
add_pepperoni = input("Voulez-vous ajouter du pepperoni ? Y ou N: ").upper()
extra_cheese = input("Voulez-vous du fromage supplémentaire ? Y ou N: ").upper()

# Initialisation du coût de la pizza
facturefinal = 0

# Calcul de la facture en fonction de la taille
if size == "S":
    facturefinal += 15
elif size == "M":
    facturefinal += 20
elif size == "L":
    facturefinal += 25
else:
    print("Taille de pizza invalide.")

# Ajout de pepperoni
if add_pepperoni == "Y":
    if size == "S":
        facturefinal += 2
    elif size in ["M", "L"]:
        bill += 3

# Ajout de fromage supplémentaire
if extra_cheese == "Y":
    facturefinal += 1

# Affichage de la facture finale
print(f"Votre facture finale est : {facturefinal} $.")