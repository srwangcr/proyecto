C = 0 

while 5>=C :
    while True: 
        try: 
         Eleccion= int(input("Ingrese un valor del 1 al 5 , con el valor 1 ingresas a la elección del paquete, con el valor 2, ingresas al horario de atención, con el valor 3, ingresas al apartado de servicios, con el valor 4 ingresas al historial y con el valor 5, ingresas a la facturación"))
         break
        except ValueError:
            print ("Por favor ingrese un número sin decimales ni letras")
    if Eleccion == 1: ##en python se compara con ==
     import Venta_de_paquete
     C= C+1
     ##Esta opción redireccionará al codigo de venta de paquete
    elif Eleccion == 2 : 
        import Horario_de_atencion
        C= C+1
        ##Esta opción redireccionará al codigo de Horario de atención
    else: 
        print ("Ingrese una opción correcta, por favor")
        C= C-1   
"""
    elif Eleccion == 3 : 
        import Servicios
        C= C+1
        ##Esta opción redireccionará al codigo de Servicios
    elif Eleccion == 4 : 
        import Historial
        C= C+1
        ##Esta opción redireccionará al codigo de historial 
    elif Eleccion == 5 : 
        import Facturacion
        C= C+1
        ##Esta opción redireccionará al codigo de facturación #"
"""
    