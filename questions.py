import random

words = {"programacion":["python","programa","variable","funcion","bucle"],"tipos de datos":["cadena","entero","lista"]}

puntaje= 0

print("¡Bienvenido al Ahorcado!")
print()
print("categorias: ")
for categoria in words:
    print(categoria)

categoria = input("elije una poniendo el nombre: ").lower() #por si el usuario pone alguna letra en mayusculas

while categoria not in words: #verifico si la categoria es valida
    print("categoria no valida")
    categoria = input("elije una poniendo el nombre: ").lower()

aleatorio = random.sample(words[categoria],len(words[categoria]))

for palabra in aleatorio: #la cantidad de rondas jugadas va a ser la cantidad de palabras en esa categoria
    word = palabra
    attempts = 6 # reinicio la cantidad de intentos 
    guessed = []  # reinicio letras usadas

    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            puntaje += 6
            print ("¡Ganaste!")
            break

        print(f"Intentos restantes: {attempts}")    
        print(f"Letras usadas: {', '.join(guessed)}")
    
        letter =input("Ingresá una letra: ")

        if len(letter) != 1 or not(letter.isalpha()): #verifico que sea 1 letra 
            print("entrada no valida")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
        print()

    else:
        puntaje = 0
        print(f"¡Perdiste! La palabra era: {word}" )
print (f"tu puntaje fue de:{puntaje}" )