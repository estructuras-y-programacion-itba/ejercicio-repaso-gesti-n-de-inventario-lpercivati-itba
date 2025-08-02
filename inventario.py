'''
En este archivo va tu solucion. Revisa las utilidades ya provistas y los helpers nuevos que puedes usar.
Recuerda que puedes crear mas funciones para solucionar el problema ;).
'''

from random import randint


# utilidades ya provistas
def strip_custom(string):
    return string.strip()


def split_custom(string, separador):
    return string.split(separador)


def buscar_producto(productos, codigo):
    for i in range(len(productos)):
        if productos[i] == codigo:
            return i
    return -1


def suma_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


# --- helpers nuevos -------------------------------------------------

def validar_entero_positivo(n):
  if not isinstance(n, int):
    return False

  return n > 0

def leer_inventario_y_historial(ruta):
    """
    Lee (o crea) inventario e historial de ventas.
    Devuelve cuatro listas paralelas.
    """
    productos, cantidades = [], []
    productos_hist, cantidades_hist = [], []

    try:
        with open(ruta, "r") as f:
            for linea in f:
                partes = split_custom(linea, ":")
                codigo = int(partes[0])
                cant = int(partes[1])

                if codigo > 0:            # item de inventario
                    productos.append(codigo)
                    cantidades.append(cant)
                else:                      # item de historial
                    productos_hist.append(-codigo)
                    cantidades_hist.append(cant)

    except FileNotFoundError:
        # inventario inicial por defecto
        for i in range(10):
            productos.append(1000 + i)
            cantidades.append(100)

    return productos, cantidades, productos_hist, cantidades_hist


def guardar_inventario_y_historial(
    ruta, productos, cantidades, productos_hist, cantidades_hist
):
    """Escribe inventario + historial nuevamente en disco."""
    with open(ruta, "w") as f:
        for i in range(len(productos)):
            f.write(f"{productos[i]}: {cantidades[i]}\n")

        for i in range(len(productos_hist)):
            f.write(f"{-productos_hist[i]}: {cantidades_hist[i]}\n")


def procesar_venta_unitaria(
    productos, cantidades, productos_hist, cantidades_hist
):
    """Realiza una venta aleatoria y actualiza listas in‑place."""
    indice = randint(0, len(productos) - 1)
    codigo = productos[indice]
    a_vender = randint(1, 5)

    # ajustar stock disponible
    if cantidades[indice] >= a_vender:
        cantidades[indice] -= a_vender
    else:
        a_vender = cantidades[indice]
        cantidades[indice] = 0

    print(f"Se vendieron {a_vender} productos de código {codigo}")

    # registrar en historial
    if a_vender > 0:
        pos = buscar_producto(productos_hist, codigo)
        if pos == -1:
            productos_hist.append(codigo)
            cantidades_hist.append(a_vender)
        else:
            cantidades_hist[pos] += a_vender


def mostrar_indice_rotacion(productos_hist, cantidades_hist):
    """Imprime el índice de rotación de productos vendidos."""
    total_vendido = suma_lista(cantidades_hist)
    productos_diferentes = len(productos_hist)

    if productos_diferentes > 0:
        indice = total_vendido / productos_diferentes
        print("El índice de rotación es: " + str(indice))
    else:
        print("No se vendió ningún producto")


#######################################################
# Tu solución debe ir aquí
#######################################################


def vender_productos(ruta, cantidad):
  """
  Gestiona el inventario de una tienda, registrando ventas, actualizando
  cantidades y calculando el índice de rotación del inventario.

  Args:
    ruta (str): La ruta del archivo de inventario.
    cantidad (int): La cantidad de productos diferentes a vender.
  """
  pass


# --- main -------------------------------------------------------------

def main():
  vender_productos("inventario.txt", "papa")
  vender_productos("inventario.txt", 3)


if __name__ == "__main__":
  main()  