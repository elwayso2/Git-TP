import random

#couleur 
text_vert: str = "\033[92m"
text_rouge: str = "\034[93m"
text_normal: str = "\033[0m"


# variable
mode_Choisi: int
nombre_random: int
nombre_guess: int
nombre_maximum: int
nombre_minimum: int = 1
essai_actuel: int = 1
essai_Maximum: int
nombre_random = random.randint(1, 20)
i: int

print(text_normal + "Choisir une des options suivantes (entrez un nombre entre 1 et 4): ")
print("1 - Facile: Nombre entre 1 et 19, 10 essais")
print("2 - Normal: Nombre entre 1 et 49, 5 essais")
print("3 - Diffile: Nombre entre 1 et 99, 5 essais")
print("4 - Impossible: Nombre entre 1 et 999, 1 essai")

mode_Choisi = int(input(""))



match mode_Choisi:
    case 1:
        essai_Maximum = 10
        nombre_maximum = 20
        nombre_random = random.randint(1, 19)
    case 2:
         essai_Maximum = 5
         nombre_maximum = 50
         nombre_random = random.randint(1, 49)
    
    case 3:
         essai_Maximum = 5
         nombre_maximum = 100
         nombre_random = random.randint(1, 99)
    case 4:
         essai_Maximum = 1
         nombre_maximum = 1000
         nombre_random = random.randint(1, 999)
    
    case _:
        print("erreur")


while essai_actuel < essai_Maximum:
    print(f"({essai_actuel} / {essai_Maximum}) {nombre_minimum} < ? < {nombre_maximum} :")
    nombre_guess = int(input(""))
    essai_actuel += 1
    if nombre_guess > nombre_random:
        nombre_maximum = nombre_guess
    elif nombre_guess < nombre_random:
        nombre_minimum = nombre_guess
    elif nombre_random == nombre_guess:
        print("vous avez gagné")
        essai_actuel = essai_Maximum + 1
    


