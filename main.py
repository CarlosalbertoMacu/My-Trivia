BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import time
import random  # Importamos la librería random
puntaje = 0

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre Naruto")
print ("Pondremos a prueba tus conocimientos de ninja")
print("Tienes", puntaje, "puntos por ahora")
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar ")
  # Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
  
  nombre = input("Ingresa tu nombre: ")
  
  # Es importante dar instrucciones sobre cómo jugar:
  # Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
  print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
  
  # OJO, el \n al final de la línea 6 es para dar un "salto de línea"
  
  # Pregunta 1
  print ("1) ¿Quién fue el primer hokage?")
  print (" a) Orochimaru")
  print (" b) Hiruzen")
  print (" c) Minato")
  print (" d) Hashirama")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  #Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_1 == "d":
    puntaje += 10
    print(GREEN+"Muy bien", nombre, "!"+RESET)
  else:
    print(RED+"Incorrecto", nombre, "!"+RESET)
  
  print(nombre, "llevas", puntaje, "puntos")
  
  # Pregunta 2
  print("\n1) ¿Quién es el ninja más fuerte?")
  print(" a) Jiraya")
  print(" b) Pain")
  print(" c) Sasuke")
  print(" d) Naruto")
  
  # Almacenamos la rspuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d", "Itachi"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    print(RED+"Incorrecto!", nombre, " Naruto es el más fuerte"+RESET)
  elif respuesta_2 == "b":
    print(RED+"Incorrecto!", nombre, "Naruto es el más fuerte"+RESET)
  elif respuesta_2 == "c":
    print(RED+"Incorrecto!", nombre, "Naruto es el más fuerte"+RESET)
  elif respuesta_2 == "Itachi":
    print(GREEN+" Dios Itachi :3"+RESET)
    puntaje +=100
  else:
    puntaje += 10
    print (GREEN+"Muy bien", nombre, "!"+RESET)
  
  print(nombre, "llevas", puntaje, "puntos")
  
  # Pregunta 3
  print ("\n1) ¿En que aldea nacio Naruto?")
  print (" a) Aldea oculta de la niebla")
  print (" b) Aldea oculta de la Arena")
  print (" c) Aldea oculta de la Hoja")
  print (" d) Aldea oculta de la Nube")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input (RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  
  if respuesta_3 == "a":
    print (RED+"Totalmente incorrecto! ..."+RESET)
    puntaje = puntaje / 2
  elif respuesta_3 == "b":
    print (RED+"Mal..."+RESET)
    puntaje = puntaje + 5
  elif respuesta_3 == "d":
    print (RED+"Incorrecto! ..."+RESET)
    puntaje = puntaje - 5
  else:
    print (GREEN+"Correcto! ..."+RESET)
    puntaje = puntaje * 2
    
  print(nombre, "llevas", puntaje, "puntos")

#ruleta
  
  print(MAGENTA+" Ahora juguemos una ruleta para probar tu suerte :3"+RESET)
  input(MAGENTA+"Presiona Enter para continuar"+RESET)
  
  z = random.randint(0, 10) * 10
  puntaje += z
  print(YELLOW+"-----------prrrrrrrrrrr----------------"+RESET)
  time.sleep(3) # Espera 3 segundos antes de continuar.
  print(YELLOW+nombre, "ganaste", z, "puntos"+RESET)
  time.sleep(3) # Espera 3 segundos antes de continuar.
  print (BLUE+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  time.sleep(2) # Espera 2 segundos antes de continuar.
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.