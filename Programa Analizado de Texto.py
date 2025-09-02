#Se debera pedir al usuario que ingrese un texto (articulo, parrafo, frase, poema, etc.)
#Ingresar 3 letras de su eleccion
#5 analisis diferentes:
#1. Cuantas veces aparece cada letra.
#2. Cuantas palabras hay dentro de todo el texto.
#3. Cual es la primera y ultima letra del texto.
#4. Palabras en orden inverso.
#5. Aparece la palabra python.

texto = input("Ingresa cualquier texto: ")
texto = texto.lower()
lista_palabras = texto.split()
letra1 = input("Ingresa cualquier letra: ").lower()
letra2 = input("Ingresa cualquier otra letra: ").lower()
letra3 = input("Ingresa cualquier otra letra: ").lower()

letra1v = texto.count(letra1)
letra2v = texto.count(letra2)
letra3v = texto.count(letra3)

print("\n")
print("CANTIDAD DE LETRAS")
print(f"La letra '{letra1}' aparece '{letra1v}' veces")
print(f"La letra '{letra2}' aparece '{letra2v}' veces")
print(f"La letra '{letra3}' aparece '{letra3v}' veces")

print("\n")
print("CANTIDAD DE PALABRAS")
print(f"La cantidad de palabras en el texto es de {len(lista_palabras)} palabras.")

print("\n")
print("LETRA DE INICIO Y FIN")
print(f"La primera letra del texto es '{texto[0]}' y la ultima letra es '{texto[-1]}'")

print("\n")
print("TEXTO INVERTIDO")
lista_palabras.reverse()
texto_invertido = " ".join(lista_palabras)
print(f"Si ordenamos tu texto al reves va a decir: {texto_invertido}")

print("\n")
print("La palabra 'python' se encuentra en tu texto: Verdadero o Falso")
buscar_python = 'pyhton' in texto
dic = {True: 'si', False: 'no'}
print(f"La palabta 'Python' {dic[buscar_python]} se encuentra en el texto")