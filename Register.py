while True: # entra en un bucle  
 nombre_user = input("Por favor ingrese su nombre completo: ") # pide tu nombre
 if all(c.isalpha() or c.isspace() for c in nombre_user): # abre un if para revisar que solo metas letras y espacios para evitar uso de numeros
   break # si todo esta bien salta al siguiente proceso
 else: # en caso de que falle le pide reingresas los datos
  print("por favor ingrese su nombre y apellido sin números")
while True: # entra en un bucle
    try: # llama a lo siguiente: 
     numero_de_cedula = int(input("Por favor ingrese su número de cedula: ")) # pide tu numero de cedula
     if numero_de_cedula < 0 : # verifica que el numero de cedula sea mayor a 0 para evitar uso de negativos
      print("el numero no puede ser negativo")
     else: 
      break # sale del bucle
    except ValueError: # esto hace una excepcion del break para manndar el siguiente print a pantalla y volver a pedir datos
         print("por favor ingrese su numero de celuda sin letras ni caracteres especiales. ")
while True: # abre bucle
    try: # llama al siguiente proceso
     numero_de_celular = int(input("Por favor ingrese su número de celular: ")) # pide el numero de celular
     if numero_de_celular < 0 : # verifica que el numero de celular sea mayor a 0 para evitar el uso de números negativos
      print("el numero no puede ser negativo") # imprime el  mensaje
     else: 
      break
    except ValueError:
     print("por favor ingrese su numero de celular sin letras ni caracteres especiales. ")



correo = str(input("Por favor ingrese su correo electronico: "))


direccion = str(input("Por favor ingrese su direccion: "))

print("nombre: " + nombre_user, "numero de cedula es: " + str(numero_de_cedula), "numero de celular es: " + str(numero_de_celular), "el correo es: " + correo, "la direccion es: " + direccion)
