class NumeroInvalidoError(Exception):
    """Excepción personalizada para manejar números no naturales."""
    pass


def obtener_numero_natural():
    while True:
        try:
            num = input("Ingrese un número natural: ")
            num = int(num)
            if num < 1:
                raise NumeroInvalidoError("Oopps!...El número debe ser un natural (mayor o igual a 1).")
            # Salimos del bucle si el número es válido
            break
        except ValueError:
            print("Entrada inválida: debe ser un número entero.")
        except NumeroInvalidoError as e:
            print(e)
        finally:
            print("Procesando...")

    return num


def calcular_divisores(num):
    divisores = []
    try:
        for i in range(1, num + 1):
            if num % i == 0:
                divisores.append(i)
    except Exception as e:
        print(f"Ocurrió un error al calcular divisores: {e}")
    else:
        print("Cálculo de divisores completado exitosamente.")
    finally:
        print("Finalizando la función de cálculo de divisores.")

    return divisores


def main():
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == "__main__":
    main()
