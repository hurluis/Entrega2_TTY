#Importar la biblioteca random
import random
#Traer el archivo de logica a nuestra consola
from LogicTTY.crear_tablero_logica import *

# Para que si no se da bien lo que está planeado, dirija al usuario al bloque de excepciones.
try:
    # Solicitar al usuario los valores de entrada
    filas = random.randint(1, 30)
    columnas = random.randint(1, 30)
    cantidad_barcos = int(input("Ingrese la cantidad de barcos: ")) 
    # Solicitar al usuario los tamaños de las naves
    tamano_naves = []
    for i in range(cantidad_barcos):
        while True:
            try:
                tamano = int(input(f"Ingrese el tamaño de la nave {i + 1} (1, 2, 4): "))
                if tamano in [1, 2, 4]:
                    tamano_naves.append(tamano)
                    break
                else:
                    print("Error: El tamaño de la nave debe ser 1, 2 o 4. Intente nuevamente.")
            except ValueError:
                print("Error: Ingrese un valor válido como número entero. Intente nuevamente.")

    # Crear el tablero
    tablero_barcos = TableroBarcos(filas, columnas)
    
    
    # Colocar barcos aleatoriamente
    barcos = []
    try:
        for tamano in tamano_naves:
            while True:
                fila = random.randint(0, filas - 1)
                columna = random.randint(0, columnas - 1)
                direccion = random.choice(["horizontal", "vertical"])
                
                try:
                    # Intenta colocar el barco en el tablero
                    barco = tablero_barcos.colocar_barco(fila, columna, tamano, direccion)
                    barcos.append(barco)
                    break
                except (ValueError, IndexError, TypeError) as e:
                    # Si hay un error al colocar el barco, muestra un mensaje de error
                    raise Exception(f"Error: {e}")

        # salidas
        print("\nTablero con barcos:")
        tablero_barcos.mostrar_tablero()

        print("\nTablero oculto:")
        tablero_barcos.mostrar_tablero_oculto()


    #Manejo de excepcion en el casode este try
    except Exception as e:
        print(f"Error: {e}")


# casos de error
except FilasColumasCeroError as fcce:
    print(f"Error: {fcce}")
except BarcoFueraTableroError as bfte:
    print(f"Error: {bfte}")
except Exception as dse:
    print(f"Error inesperado: {dse}")