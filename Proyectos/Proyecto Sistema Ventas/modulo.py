def ingresar_ventas(lista_ventas):
    while True:
        try:
            curso = input ('Íngrese el nombre del curso: ').upper()
            cantidad = int (input('Ingrese la cantidad de curso vendidos: '))
            fecha = input('Íngrese la fecha de la venta (AAAA-MM-DD): ')
            precio = float(input('Íngrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente: ').upper()
        except ValueError:
            print('Entradas no invalidas, por favor intentelo nuevamente')
            continue        
        
        venta = {
            'curso' : curso,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
            'cliente' : cliente
        }
        lista_ventas.append(venta)
        
        continuar = input('Desea ingresar otra venta s/n :').lower()
        if continuar == 's':
            print('\n---- Ingresando otra venta ----')
        elif continuar == 'n':
            break
        else: 
            print ('Opción no valida')