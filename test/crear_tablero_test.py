# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
#Lo importamos para incluir la ruta de busqueda de python
import sys
sys.path.append("src")
#Importar archivo de lógicxa para hacer las pruebas
import LogicTTY.crear_tablero_logica as crear_tablero_logica
from LogicTTY.crear_tablero_logica import *
#Se crea la clase para hacer las pruebas con la biblioteca unittest
class DispararTest(unittest.TestCase):

    #Este metodo de aca se coloca, para que cada test se le pueda asignar un tamaño personalizado si asi se desea 
    def set_tamaño_tablero(self, filas, columnas):
        self.tablero = TableroBarcos(filas, columnas) 

    #Test asegura que el tablero se este creando correctamente
    def test_creacion_tablero(self):
        filas=8
        columnas=8
        tablero = TableroBarcos(filas, columnas)
        self.assertEqual(len(tablero.tablero), filas)
        self.assertEqual(len(tablero.tablero[0]), columnas)
      
    #Test evalua que un barco pueda colocarse en el limite
    def test_colocar_barco_en_limite(self):
        # Prueba que se pueda colocar un barco en el límite del tablero
        tablero = TableroBarcos(5, 5)
        tablero.colocar_barco(0, 0, 3, 'horizontal')
        # Verificar que el barco se haya colocado correctamente en las posiciones esperadas
        self.assertEqual(tablero.tablero[0][0], 'X')
        self.assertEqual(tablero.tablero[0][1], 'X')
        self.assertEqual(tablero.tablero[0][2], 'X')
        

    #test verifica que el tablero no tenga barcos sino se ingresan barcos
    def test_TableroVacio(self):
        filas=20
        columnas=20
        # Tablero sin barcos
        tablero = TableroBarcos(filas, columnas)
        # Verificar que el tablero está vacío
        for fila in tablero.tablero:
            self.assertEqual(fila, ['O'] * 20)


     # Test asegura que se pueda crear un tablero de 1x1 correctamente
    def test_Tablero1x1(self):
        # Número de filas y columnas válidas
        filas = 1
        columnas = 1
        # Coordenadas válidas de los barcos
        fila = 0
        columna = 0
        tamaño = 1
        direccion = 'horizontal'
        # Crear el tablero
        tablero = TableroBarcos(filas, columnas)
        # Intentar colocar el barco en el tablero
        tablero.colocar_barco(fila, columna, tamaño, direccion)
        # Verificar que el tablero ahora tiene un barco en la posición (0, 0)
        self.assertEqual(tablero.tablero, [['X']])


# Test valida que se puedan ingresar 10000 posiciones
    def test_10milX10mil(self):
        # Número de filas y columnas válidas
        filas = 10000
        columnas = 10000
        # Crear el tablero
        tablero = TableroBarcos(filas, columnas)
        # Verificar que el tablero se haya creado correctamente
        self.assertEqual(len(tablero.tablero), filas)
        self.assertEqual(len(tablero.tablero[0]), columnas)


    # Test valida si funciona correctamente la colocación de los barcos en la misma fila
    def test_BarcosMismaFilaColumna(self):
        # Número de filas y columnas válidas
        filas = 3
        columnas = 4
        # Coordenadas válidas de los barcos
        fila = 1
        columna = 0  
        tamano = 4
        direccion = 'horizontal'
        # Crear tablero
        tablero = TableroBarcos(filas, columnas)
        # Intentar colocar los barcos en el tablero
        tablero.colocar_barco(fila, columna, tamano, direccion)
        # Verificar que el tablero se actualizó correctamente
        self.assertEqual(tablero.tablero, [['O', 'O', 'O', 'O'], ['X', 'X', 'X', 'X'], ['O', 'O', 'O', 'O']])


    # Test valida si se lanza una excepción al ingresar un valor no entero
    def test_IngresoStr(self):
        # Número de filas y columnas válidas
        filas = "dos"
        columnas = "tres"
        # Verificar que se lanza una excepción al intentar crear el tablero
        with self.assertRaises(Exception):
            TableroBarcos(filas, columnas)


    #Test que valida que se lance la excepcion de error para cuando se le de una dirección al barco
    def test_direccion_no_valida(self):
        # Crear un tablero 5x5
        tablero = TableroBarcos(5, 5)
        
        # Coordenadas y tamaño de un barco
        fila = 2
        columna = 2
        tamano = 3
        
        # Dirección no válida
        direccion = 'diagonal'
        
        # Verificar que se lance ValueError con la dirección no válida
        with self.assertRaises(ValueError):
            tablero.colocar_barco(fila, columna, tamano, direccion)

    #Test controla el error donde las filas son 0
    def test_validar_tamaño_filas_cero(self):
        tablero = TableroBarcos(filas=0, columnas=10)
        with self.assertRaises(FilasColumasCeroError):
            tablero.validar_tamaño()


    #Test controla la excepcion de la columna no puede ser negadiva
    def test_validar_tamaño_columnas_negativas(self):
        tablero = TableroBarcos(filas=20, columnas=-1)
        with self.assertRaises(FilasColumasCeroError):
            tablero.validar_tamaño()
   
if __name__ == '__main__':
    unittest.main()