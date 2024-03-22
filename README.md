# Documentación del Juego de Batalla Naval

## Descripción
Este proyecto consiste en la implementación de un juego de batalla naval en Python. El juego permite a un jugador intentar hundir todos los barcos en un tablero de 10x10 utilizando coordenadas de disparo.

## Requisitos del Sistema
- Python 3.x

## Instrucciones de Instalación
1. Descarga el archivo del proyecto desde [enlace al repositorio].
2. Abre una terminal y navega hasta el directorio del proyecto.
3. Ejecuta el juego utilizando el comando `python jugar_consola.py`.

## Estructura del Código
El código está organizado en tres archivos principales:
- `crear_tablero_logica.py`: Contiene la lógica para crear el tablero de juego.
- `disparar_logica.py`: Contiene la lógica para realizar disparos en el juego.
- `jugar_consola.py`: El punto de entrada del juego que gestiona la interacción con el usuario.

## Descripción de las Clases y Funciones Principales
### Clase TableroBarcos
Esta clase representa el tablero de juego y proporciona métodos para inicializar y mostrar el tablero.

- `__init__(self, tamaño)`: Constructor de la clase. Crea un tablero de barcos con el tamaño especificado.
- `mostrar_tablero(self)`: Método para imprimir el tablero en la consola.

### Clase Disparar
Esta clase permite realizar disparos en el tablero de juego y verificar si un disparo acierta a un barco.

- `__init__(self, x, y, tablero)`: Constructor de la clase. Crea un objeto Disparar con las coordenadas y el tablero.
- `shoot(self)`: Método para realizar un disparo en las coordenadas especificadas.
- `check_impact(self)`: Método para verificar si el disparo acierta a un barco.
- `game_over(self)`: Método para verificar si todos los barcos han sido hundidos.

## Ejemplos de Uso
Para iniciar el juego, ejecuta el script `jugar_consola.py` desde la terminal. A continuación, sigue las instrucciones en pantalla para ingresar las coordenadas de tus disparos.
