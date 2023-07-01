import string
import random

lettres = string.ascii_letters
chiffres = string.digits
ponc = string.punctuation

while True:
    try:
        ulettres = eval(input("Lettres (True ou False): "))
        uchiffres = eval(input("Chiffres (True ou False): "))
        uponc = eval(input("Ponctuation (True ou False): "))

        l = int(input("Longueur du mot de passe: "))
        
        # Ajouter des lettres possibles
        char = ""
        char += lettres if ulettres else ""
        char += chiffres if uchiffres else ""
        char += ponc if uponc else ""
        passe = "".join(random.choices(char, k=l)) # Générer le mot de passe
        print(passe) # Imprimer le nouveau mot de passe
    except:
        print("Veuillez suivre les instructions")
        
    try:
        if eval(input("Quitter (True ou False): ")):
            break
    except:
        print("Veuillez suivre les instructions")