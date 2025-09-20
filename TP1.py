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
nombre_minimum: int
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
        nombre_minimum = 0
        nombre_maximum = 20
        for essai_actuel in range(1 , 11 , +1):
            print(f"{essai_actuel} / {essai_Maximum} {nombre_minimum} < ? < {nombre_maximum} :")
            nombre_guess = int(input(""))
            if nombre_guess == nombre_random:
                print("vous avez gagné")
            elif nombre_guess <= nombre_random:
                nombre_guess = nombre_minimum + 0
            elif nombre_guess >= nombre_random:
                nombre_guess = nombre_maximum + 0
            elif essai_actuel == essai_Maximum:
                print(f"vous avec perdu le nombre était {nombre_random}")
    # case 2:
    
    # case 3:
    
    # case 4:
    
    case _:
        print("erreur")