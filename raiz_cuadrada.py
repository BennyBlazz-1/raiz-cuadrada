import math

def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.

    Parámetros:
    numero (int o float): El número del cual se desea calcular la raíz cuadrada.

    Retorna:
    float: La raíz cuadrada del número proporcionado.

    Lanza:
    TypeError: Si el número no es un entero o un flotante.
    ValueError: Si el número es negativo.
    """

    # Validar tipo
    if not isinstance(numero, (int, float)):
        raise TypeError("El número debe ser entero o decimal.")
    
    # Validar número negativo
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    
    return math.sqrt(numero)
