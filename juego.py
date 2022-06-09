# juego del ahorcado
# @lauradaniela
"""
explicacion.
1. elegir aleatoriamente una palabra de una lista de palabras.
2. Mostrar el dibujo de una horca.
3. Mostrar un guion bajo por cada letra de la palabra.
4. Pedir al usuario que introduzca una letra: si no es una unica letra indicarlo. si ya se ha dicho indicarlo.
5. Comprobar si esa letra esta contenida en la palabra elegida.
6. Si esta: volover a mostrar el dibujo de la horca como la ultima vez.
sustituir el guion correspondiente por la letra dicha. 
7. Si la palabra no esta: Mostrar el dibujo de la hora al que se añade una parte.
8. Si se falla 6 veces: se completa el dibujo del ahorcado.
9. Si se aciertan todas las letras de la palabra: Ganó!
"""
import random
import os

palabras = ["COLOMBIA","ECUADOR","VENEZUELA","BRASIL","ARGENTINA","PERU","CHILE","BOLIVIA","PARAGUAY","URUGUAY","GUYANA","SURINAM"]

palabra = random.choice(palabras)

fallo0 = """
          !===N
              N
              N
              N
      =========
"""
fallo1 = """
          !===N
          O   N
              N
              N
      =========
"""
fallo2 = """
          !===N
         _O   N
              N
              N
      =========
"""
fallo3 = """
          !===N
         _O_  N
              N
              N
      =========
"""
fallo4 = """
          !===N
         _O_  N
          |   N
              N
      =========
"""
fallo5 = """
          !===N
         _O_  N
          |   N
         /    N
      =========
"""
fallo6 = """
          !===N
         _O_  N
          |   N
         / \  N
      =========
"""
letras_correctas = "" # letras correctas dichas por el usuario
letras_todas = "" # todas las letras dichas por el usuario
fallos = 0 
while True:
  os.system("cls")
  print("************************")
  print("** JUEGO DEL AHORCADO **")
  print("************************")
  if fallos == 0:
    print(fallo0)
  elif fallos == 1:
    print(fallo1)
  elif fallos == 2:
    print(fallo2)
  elif fallos == 3:
    print(fallo3)
  elif fallos == 4:
    print(fallo4)
  elif fallos == 5:
    print(fallo5)  
  elif fallos == 6:
    print(fallo6)

  print()

  # Mostramos las letras acertadas y guiones bajos en las no acertadas

  resultado = ""

  for letra in palabra:
    if letra in letras_correctas:
      resultado += letra
    else:
      resultado += "_"
  print("    {}".format(resultado))
  print()
  print()

  # comprobamos si se ha acertado la palabra o se han terminado los intentos
  if resultado == palabra:
     print("*** HAS GANADO ***")
     break
  if fallos > 5:
     print("la palabra es: ", palabra)
     print("*** HAS PERDIDO ***")
     break

  # bucle para que el usuario teclee una letra que cumpla los requisitos 
  while True:
    letra_usuario_sin_formato = input("Dime una letra: ")
    letra_usuario = letra_usuario_sin_formato . upper()
    if len(letra_usuario) < 1 or len(letra_usuario) >1:
      print("Introduce una letra")
    elif letra_usuario in letras_todas:
      print("Esa letra ya la has dicho")
    elif not letra_usuario.isalpha():
      print("Introduce una letra")
    else:
      letras_todas += letra_usuario
      break

  # Comprobamos si la letra dicha por el usuario esta en la palabra
  if letra_usuario not in palabra:
    fallos += 1
  else:
    letras_correctas += letra_usuario