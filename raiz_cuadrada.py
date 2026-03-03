import math


def raiz_cuadrada(numero: float) -> float:
    """
    Calcula la raíz cuadrada de un número.

    Parámetros:
    numero (int o float): Número del cual se desea obtener la raíz cuadrada.

    Retorna:
    float: Raíz cuadrada del número.

    Lanza:
    TypeError: Si el argumento no es numérico.
    ValueError: Si el número es negativo.
    """

    if not isinstance(numero, (int, float)):
        raise TypeError("El valor debe ser un número entero o decimal.")

    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")

    return math.sqrt(numero)


def mostrar_menu():
    """Muestra el menú principal."""
    print("=== CALCULADORA DE RAÍZ CUADRADA ===")
    print("1. Calcular raíz cuadrada")
    print("2. Salir")


def ejecutar_aplicacion():
    """Ejecuta la aplicación interactiva en consola."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                valor = input("Ingresa un número: ")
                numero = float(valor)

                resultado = raiz_cuadrada(numero)
                print(f"✅ La raíz cuadrada de {numero} es: {resultado:.4f}")

            except ValueError as ve:
                print(f"❌ Error: {ve}")
            except TypeError as te:
                print(f"❌ Error: {te}")
            except Exception as e:
                print(f"⚠ Error inesperado: {e}")

        elif opcion == "2":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    ejecutar_aplicacion()