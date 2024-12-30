from random import randint

# Générer un nombre aléatoire entre 0 et 100
nombreAleatoire = randint(0, 100)

#Nombre d'essai de l'utilisateur
essai = 5

print("*** Le jeu du nombre mystère ***")
while essai != 0:
    
    #Demande à l'utilisateur de saisir un nombre
    nb1 = int(input("Veuillez saisir une premiere valeur = "))

    if nombreAleatoire > nb1:
        print(f"Le nombre est plus grand que {nb1}")
    elif nombreAleatoire < nb1:
        print(f"Le nombre est plus petit que {nb1}")
    else:
        print("Bien joué, tu as trouvé le nombre mystère")
        break

    essai -= 1

if essai == 0:
    print(f"Dommage! le nombre mystère était {nombreAleatoire}")
else:
    print(f"Bravo! le nombre mystère était {nombreAleatoire} !")
    print(f"Tu as trouvé le nombre, il te reste {essai} essai")




 