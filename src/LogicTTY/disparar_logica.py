# Importar la clase TableroBarcos del módulo crear_tablero_logica
from LogicTTY.crear_tablero_logica import TableroBarcos

# Definir excepciones personalizadas
class CoordenadasFueraRangoError(IndexError):
    def __str__(self):
        return "Error: Las coordenadas ingresadas para el disparo están fuera del rango del tablero de juego."

class CoordenadasValorIncorrecto(ValueError):
    def __str__(self):
        return "Error: Las coordenadas ingresadas no son de tipo entero (int) y deben serlo."

class CoordenadasNegativas(Exception):
    def __str__(self):
        return "Error: Las coordenadas ingresadas fueron negativas y deben ser positivas."

class ErrorMasDeDosCoordenadas(Exception):
    def __str__(self):
        return "Error: Se ingresaron más de dos coordenadas. Solo se permite ingresar un número entero por coordenada."

# Definir la clase principal para disparar
class Disparar:
    # Método inicializador de la clase Disparar
    def __init__(self, x, y, tablero: TableroBarcos):
        # Inicializar coordenadas X e Y del disparo, último disparo X e Y, y el tablero
        self.coordenadaX = x
        self.coordenadaY = y
        self.ultimoDisparoX = 0
        self.ultimoDisparoY = 0
        self.tablero = tablero

    # Método que realiza el disparo
    def shoot(self):
        # Actualizar las coordenadas del último disparo
        self.ultimoDisparoX = self.coordenadaX
        self.ultimoDisparoY = self.coordenadaY

        # Convertir las coordenadas a enteros si son flotantes
        if isinstance(self.coordenadaX, float):
            self.coordenadaX = int(self.coordenadaX)
          
        if isinstance(self.coordenadaY, float):
            self.coordenadaY = int(self.coordenadaY)

        # Validar que las coordenadas sean enteros
        if not isinstance(self.coordenadaX, int) or not isinstance(self.coordenadaY, int):
            raise CoordenadasValorIncorrecto

        # Validar que las coordenadas no sean negativas
        if self.coordenadaX < 0 or self.coordenadaY < 0:
            raise CoordenadasNegativas()

        # Validar que las coordenadas estén dentro del rango del tablero
        if self.coordenadaX >= len(self.tablero.tablero) or self.coordenadaY >= len(self.tablero.tablero[self.coordenadaX]):
            raise CoordenadasFueraRangoError
    
        # Realizar el disparo y actualizar el tablero
        if self.check_impact():
            self.tablero.tablero[self.coordenadaX][self.coordenadaY] = '*'
            if self.game_over():
                return None
            return True
        else:
            if self.game_over():
                return None
            return False

    # Método para verificar si el disparo impacta un barco
    def check_impact(self):
        if self.tablero.tablero[self.coordenadaX][self.coordenadaY] == 'O':
            return False
        if self.tablero.tablero[self.coordenadaX][self.coordenadaY] == 'X':
            return True

    # Método para verificar si todos los barcos han sido destruidos
    def game_over(self):
        if any('X' in row for row in self.tablero.tablero):
            return False
        else:
            return True
