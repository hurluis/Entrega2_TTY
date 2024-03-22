# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
#Lo importamos para incluir la ruta de busqueda de python
import sys
sys.path.append("src")
#Importar archivo de lógicxa para hacer las pruebas
import LogicTTY.disparar_logica as disparar_logica
from LogicTTY.disparar_logica import *


# 2. Construir clase de pruebas
# Esta clase sirve para crear un tablero para estas pruebas
class Tablero:
    def __init__(self,tablero):
        self.tablero=tablero


# 2.1. Construir clase de pruebas
class JuegoTTYTests ( unittest.TestCase ):
# 3. Crear metodos de prueba

    # Prueba para verificar si un disparo impacta un objetivo
    def test_disparar_objetivo_exitoso(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas del disparo
        disparo = Disparar(0, 3, tablero)
        # Disparo exitoso
        resultado = disparo.shoot()
        self.assertTrue(resultado)

    # Prueba para verificar si un disparo falla al no impactar un objetivo
    def test_disparar_objetivo_fallido(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas del disparo
        disparo = Disparar(1, 5, tablero)
        # Disparo fallido
        resultado = disparo.shoot()
        self.assertFalse(resultado)

    # Prueba para verificar si se levanta la excepción al ingresar coordenadas negativas
    def test_disparar_excepcion_negativos(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas negativas
        with self.assertRaises(CoordenadasNegativas):
            Disparar(2, -2, tablero).shoot()

    # Prueba para verificar si se levanta la excepción al ingresar coordenadas fuera de rango
    def test_disparar_excepcion_fuera_de_rango(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas fuera de rango
        with self.assertRaises(CoordenadasFueraRangoError):
            Disparar(4, 7, tablero).shoot()

    # Prueba para verificar si se levanta la excepción al ingresar coordenadas no enteras
    def test_disparar_excepcion_valor_incorrecto(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas incorrectas (no enteras)
        with self.assertRaises(CoordenadasValorIncorrecto):
            Disparar(3, "6", tablero).shoot()

    # Prueba adicional para verificar si un disparo impacta un objetivo
    def test_disparar_objetivo_exitoso_2(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas del disparo
        disparo = Disparar(3, 3, tablero)
        # Disparo exitoso
        resultado = disparo.shoot()
        self.assertTrue(resultado)

    # Prueba adicional para verificar si un disparo falla al no impactar un objetivo
    def test_disparar_objetivo_fallido_2(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas del disparo
        disparo = Disparar(0, 0, tablero)
        # Disparo fallido
        resultado = disparo.shoot()
        self.assertFalse(resultado)

    # Prueba adicional para verificar si se levanta la excepción al ingresar coordenadas fuera de rango
    def test_disparar_excepcion_fuera_de_rango_2(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas fuera de rango
        with self.assertRaises(CoordenadasFueraRangoError):
            Disparar(4, 7, tablero).shoot()

    # Prueba adicional para verificar si se levanta la excepción al ingresar coordenadas no enteras
    def test_disparar_excepcion_valor_incorrecto_2(self):
        # Configuración del tablero
        tablero = Tablero(tablero=[
            ["O", "O", "O", "X", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O"]
        ])
        # Coordenadas incorrectas (no enteras)
        with self.assertRaises(CoordenadasValorIncorrecto):
            Disparar(3, "6", tablero).shoot()
            

    # Prueba adicional para verificar si el juego termina cuando se destruyen todos los barcos
    def test_fin_del_juego(self):
        # Configuración del tablero con todos los barcos destruidos
        tablero = Tablero(tablero=[
            ["*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*"]
        ])
        # Disparo a cualquier posición (el juego debería haber terminado)
        resultado = Disparar(0, 0, tablero).shoot()
        # Se espera que el resultado sea None, indicando que el juego ha terminado
        self.assertIsNone(resultado)

    # Prueba adicional para verificar si el juego continúa cuando no se destruyen todos los barcos
    def test_juego_continua(self):
        # Configuración del tablero con al menos un barco restante
        tablero = Tablero(tablero=[
            ["O", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "X", "*", "*"],
            ["*", "*", "*", "*", "*", "*"]
        ])
        # Disparo a cualquier posición (el juego debería continuar)
        resultado = Disparar(0, 0, tablero).shoot()
        # Se espera que el resultado sea True o False, indicando que el juego continúa
        self.assertIsNotNone(resultado)

if __name__ == '__main__':
    unittest.main()
