# On crée une "boîte" pour chaque info
produit = input("Nom du produit : ")

# On transforme le texte en chiffre avec float() et int()
prix = float(input("Prix unitaire : "))
quantite = int(input("Quantité vendue : "))

# On fait le calcul
total = prix * quantite

# On affiche le résultat final
print("--- FACTURE ---")
print("Produit :", produit)
print("Total à payer :", total, "FCFA")