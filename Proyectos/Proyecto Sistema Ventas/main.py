"""
Sistema de Gestión de Ventas que nos permita ingresar, almacenar y analizar datos de ventas.
Autor: Eyner Serrano
Fecha: 2025-04-16
Versión: 0.1
"""
import os
from modulo import ingresar_ventas, guardar_ventas,analisis_ventas


def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecucio"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\nPresione ENTER para continuar...')


#Menu Principal
def menu():
    ventas = []
    while True:
        print('\n----- Menú Pricipal -----')
        print('1. Ingresar ventas de cursos UMCA')
        print('2. Guardar datos en un archivo CSV')
        print('3. Analizar ventas')
        print('4. Salir')
        opcion = input('Ingrese una opción: ')
        
        if opcion == "1":
            limpiar_pantalla()
            print('\n --- Ingreso de Ventas de curso ---')
            ingresar_ventas(ventas)
            pausar()
        elif opcion == "2":
            limpiar_pantalla()
            print('\n --- Guardar Ventas en CSV ---')
            guardar_ventas(ventas)
            pausar()
        elif opcion == "3":
            limpiar_pantalla()
            print('\n --- Analisis de Ventas ---')
            analisis_ventas()
            pausar()
        elif opcion == "4":
            print('\n --- Gracias por usar el sistema. Hasta Pronto!')
            pausar()
            break #< Cierro el sistema deteniendo el ciclo
        
        else:
            print('Opción no válida. Intente nuevamente una opción!')
            pausar()
        
        

#Ejecución del sistema si solo si el archivo es el main

if __name__ == '__main__':
    print('Bienvenido al sistema de Gestión de Ventas')
    pausar()
    menu()