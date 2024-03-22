#Importación de las bibliotecas 
import random
import sys
import os

# Agregar el directorio padre al path para permitir importaciones relativas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LogicTTY.crear_tablero_logica import *
from LogicTTY.disparar_logica import Disparar
from LogicTTY.disparar_logica import CoordenadasFueraRangoError, CoordenadasValorIncorrecto, CoordenadasNegativas

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



# Función para leer las coordenadas del jugador desde la consola
# casos de error
except FilasColumasCeroError as fcce:
    print(f"Error: {fcce}")
except BarcoFueraTableroError as bfte:
    print(f"Error: {bfte}")
except Exception as dse:
    print(f"Error inesperado: {dse}")



def leer_coordenadas():
    
    """
    Lee las coordenadas del jugador desde la consola.
    
    Returns:
        tuple: Coordenadas X e Y del disparo.
        
    Raises:
        CoordenadasValorIncorrecto: Si las coordenadas no son enteros.
    """
    try:
        # Solicitar al usuario que ingrese las coordenadas X e Y del disparo
        x = int(input("Ingrese la coordenada vertical del disparo: "))
        y = int(input("Ingrese la coordenada horizontal del disparo: "))
        
        # Devolver las coordenadas ingresadas
        return x, y

    # Capturar la excepción en caso de que las coordenadas no sean enteros
    except ValueError:
    # Lanzar una excepción personalizada para indicar que las coordenadas no son de tipo entero
        raise CoordenadasValorIncorrecto()

def jugar_batalla_naval(tablero: TableroBarcos):

    """
    Función principal del juego de batalla naval.
    
    Args:
        tablero (TableroBarcos): El tablero de barcos del juego.
    """

#ciclo para seguir en juego despues de cada respuesta a menos que se responda si a la pregunta de salir
    while True:
        try:
            # Leer coordenadas ingresadas por el usuario
            x, y = leer_coordenadas()

            # Crear objeto Disparar ajustando las coordenadas a índices de lista (empezando en 0)
            disparo = Disparar(x - 1, y - 1, tablero)

            # Realizar disparo y obtener resultado
            resultado = disparo.shoot()

            # Mostrar mensaje de acierto si el disparo es exitoso
            if resultado is True:
                print("¡Has acertado!")
                tablero.mostrar_tablero()

            # Mostrar mensaje de fallo si el disparo no es exitoso
            elif resultado is False:
                print("Has fallado el disparo.")
                tablero.mostrar_tablero()

            # Mostrar mensaje de fin del juego si todos los barcos han sido destruidos
            elif resultado is None:
                print("¡Fin del juego! Todos los barcos han sido destruidos.")
                break  # Salir del bucle del juego

            # Preguntar al usuario si desea salir del juego
            respuesta = input("¿Desea salir del juego? (s/n): ")
            if respuesta.lower() == "s":
                print("¡Gracias por jugar!")
                break  # Salir del bucle del juego

        # Manejar excepciones
        except CoordenadasFueraRangoError:
            print("Error: Las coordenadas ingresadas están fuera del rango del tablero de juego.")
        except CoordenadasValorIncorrecto:
            print("Error: Las coordenadas ingresadas no son de tipo entero (int) y deben serlo.")
        except CoordenadasNegativas:
            print("Error: Las coordenadas ingresadas fueron negativas y deben ser positivas.")


# Ejecutar el juego
if __name__ == "__main__":
    jugar_batalla_naval(tablero_barcos)

