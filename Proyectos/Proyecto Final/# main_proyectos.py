#Eyner Serrano Soza
#Version: 1.1
#Created on: 2025-26-04


import csv, os, matplotlib.pyplot as plt, pandas as pd

def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecucio"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\nPresione ENTER para continuar...')

# CSV donde se guardará el registro de los pagos
archivo_pagos = 'pagos.csv'

# Verificación de la existencia de la lista
def cargar_pagos():
    if os.path.exists(archivo_pagos):
        with open(archivo_pagos, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            return [pago for pago in lector]
    return []

# Guardado de los pagos
def guardar_pagos():
    with open(archivo_pagos, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'cantidad', 'fecha', 'pais', 'estatus', 'agente']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        
        escritor.writeheader()
        for pago in pagos:
            escritor.writerow(pago)

#Este es el registro de un pago nuevo donde se solicita la información al usuario y datos del pago
pagos = cargar_pagos()

def registrar_pago():

    nombre = input("Ingrese el nombre de la persona que aplica el pago: ")
    cantidad = float(input("Ingrese la cantidad del pago: "))
    fecha = input("Ingrese la fecha del pago (Formato: YYYY-MM-DD): ")
    pais = input("Ingrese el nombre del pais proveniente: ")
    estatus = input("Ingrese el estado del pago (reconciled o unreconciled): ")
    agente = input("Ingrese el agente al que pertenece el pago: ")
    
    # Agregando a la lista creada previamente
    pagos.append({"nombre": nombre, 
                  "cantidad": cantidad, 
                  "fecha": fecha,
                  "pais": pais,
                  "estatus": estatus,
                  "agente": agente})
    guardar_pagos()
    print("Pago registrado con éxito.")

def mostrar_pagos():

    if not pagos:
        print("No se han registrado pagos.")
        return
    
    print("\nPagos registrados:")
    for pago in pagos:
        print(f"Nombre: {pago['nombre']}, Cantidad: {pago['cantidad']}, Fecha: {pago['fecha']}")

def eliminar_pago():

    nombre = input("Ingrese el nombre de la persona cuyo pago desea eliminar: ")
    fecha = input("Ingrese la fecha del pago a eliminar (Formato: YYYY-MM-DD): ")
    
    # Encontrar el pago a eliminar
    global pagos
    pagos = [pago for pago in pagos if not (pago['nombre'] == nombre and pago['fecha'] == fecha)]
    guardar_pagos()  # Guardado despues de la eliminación, lista actializada.
    print("Pago eliminado (si existía).")

def editar_pago():

    nombre = input("Ingrese el nombre de la persona cuyo pago desea editar: ")
    fecha = input("Ingrese la fecha del pago a editar (Formato: YYYY-MM-DD): ")

    # Pago a editar
    for pago in pagos:
        if pago['nombre'] == nombre and pago['fecha'] == fecha:
            nueva_cantidad = float(input("Ingrese la nueva cantidad del pago: "))
            pago['cantidad'] = nueva_cantidad
            guardar_pagos()
            print("Pago actualizado.")
            return
    
    print("Pago no encontrado.")
    
def analisis_pagos():
    # Convirtiendo en un DF
    df = pd.DataFrame(pagos)
    
    # Convirtiendo la columna columna cantidad
    df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')
    
    # Agrupar por país y sumar las cantidades
    pagos_por_pais = df.groupby('pais')['cantidad'].sum()
    
    # Crear la gráfica de barras
    plt.figure(figsize=(10, 5))
    pagos_por_pais.plot(kind='bar')
    plt.title('Total Pagado por País')
    plt.xlabel('País')
    plt.ylabel('Cantidad Pagada')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def main():

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Registrar pago")
        print("2. Mostrar pagos")
        print("3. Eliminar pago")
        print("4. Editar pago")
        print("5. Mostrar analisis de pagos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            limpiar_pantalla()
            print('-------Inicie el registro del pago-------')
            registrar_pago()
            pausar()
        elif opcion == '2':
            limpiar_pantalla()
            print('-------Mostrando pagos-------')
            mostrar_pagos()
            pausar()
        elif opcion == '3':
            limpiar_pantalla()
            print('-------Proceda a ingresar los datos del pago que desea eliminar-------')
            eliminar_pago()
            pausar()
        elif opcion == '4':
            limpiar_pantalla()
            print('-------Ingrese los datos del pago que desea editar-------')
            editar_pago()
            pausar()
        elif opcion == '5':
            limpiar_pantalla()
            print('-------Presentando analisis de pagos-------')
            analisis_pagos()
            pausar()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()