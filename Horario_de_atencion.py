print ("Siempre se realizará el Check in 3pm y check out 11am y Room service de 6am a 11pm desayunos 6am a 10:30, almuerzos 12pm a 3pm")
print ("Horario 1: Spa 10am a 11am, Uso de Gimnasio 6am a 8am, Cargador eléctrico 6am a 10am, Restaurante Premium (Cena) 6pm a 7:30pm")
print ("Horario 2: Spa 2pm a 3pm Gimnasio de 9am a 11am, Cargador eléctrico 10am a 2pm, Restaurante Premium (Cena) 7:30pm a 9pm")
print ("Horario 3: Spa 6pm a 7pm, Gimnasio de 2pm a 6pm, Cargador eléctrico 2pm a 6pm, Restaurante Premium (Cena) 9pm a 10:30pm")
C= 0 
while C == 0: ##Este while sigue la misma lógica que el while definido en venta de paquete
    while True: 
        try: 
         Horario= int(input("Ingrese un valor del 1 al 3, el valor que escogas será el horario que tendrás "))
         break
        except ValueError:
            print ("Por favor ingrese un número sin decimales ni letras")
    if Horario== 1: 
        Horario_Final= str("Horario 1: Spa 10am a 11am, Uso de Gimnasio 6am a 8am, Cargador eléctrico 6am a 10am, Restaurante Premium (Cena) 6pm a 7:30pm")
        print ("Usted eligió el horario 1 ")
        C=1
    elif Horario == 2: 
        Horario_Final= str("Horario 2: Spa 2pm a 3pm Gimnasio de 9am a 11am, Cargador eléctrico 10am a 2pm, Restaurante Premium (Cena) 7:30pm a 9pm")
        print ("Usted eligió el horario 2 ")
        C=1
    elif Horario == 3: 
        Horario_Final= str("Horario 3: Spa 6pm a 7pm, Gimnasio de 2pm a 6pm, Cargador eléctrico 2pm a 6pm, Restaurante Premium (Cena) 9pm a 10:30pm")
        print ("Usted eligió el horario 3 ")
        C=1 
    else: 
        print ("Por favor, eliga un número valido para el sistema ")
        