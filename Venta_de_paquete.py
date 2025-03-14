print (" 1. Paquete 1: Incluye una estadía de 1 noche, con desayuno incluido (200$)" "2. Paquete 2: Comprende una estadía de 3 noches, con desayunos incluidos y derecho a una cena en el restaurante premium. (570$);" "3. Paquete 3: Ofrece una estadía de 5 noches, con desayunos incluidos, dos cenas en el restaurante premium y una hora de masajes relajantes en el spa. (925$)" "4. Paquete 4: Proporciona una estadía de 7 noches con desayunos incluidos, tres cenas en el restaurante premium, una hora de masajes relajantes en el spa (1260$)" )
C= 0
while C == 0: 
    while True: ##Este while asegura que no se ingrese un valor flotante o string 
        try:   
          Paquete= int(input("Ingrese el paquete deseado "))
          break ##El break hace que, si se ingresa un valor entero, sale del while true 
        except ValueError:
            print ("Ingrese el número del paquete sin decimales ni letras")
    if Paquete == 1 : ##Todos estos ifs son elecciones de paquetes
        Paquete_Seleccionado= str("Usted ha seleccionado el Paquete número 1: Estadía de 1 noche, con desayuno incluido (200$")
        Paquete_Precio= 200 
        C = 1 
        print ("Usted ha elegido el paquete 1")
    elif Paquete == 2: 
        Paquete_Seleccionado= str("Usted ha seleccionado el Paquete número 2: Estadía de 3 noches, con desayunos incluidos y derecho a una cena en el restaurante premium. (570$)")
        Paquete_Precio= 570 
        C = 1 
        print ("Usted ha elegido el paquete 2")
    elif Paquete == 3: 
        Paquete_Seleccionado= str("Usted ha seleccionado el Paquete número 3: Estadía de 5 noches, con desayunos incluidos, dos cenas en el restaurante premium y una hora de masajes relajantes en el spa. (925$)")
        Paquete_Precio= 925 
        C = 1
        print ("Usted ha elegido el paquete 3")
    elif Paquete == 4: 
        Paquete_Seleccionado= str("Usted ha seleccionado el Paquete número 4: Estadía de 7 noches con desayunos incluidos, tres cenas en el restaurante premium, una hora de masajes relajantes en el spa (1260$)" )
        Paquete_Precio= 1260
        C = 1 
        print("usted a elegido el paquete 4")
    else: 
        print ("Por favor, eliga un número valido para el sistema") ##Como la variable contadora no cambió de 0, se repite el primer while
                                                                    ##junto con el segundo while, asegurando a la vez, que el valor no se exceda de 1 a 4.