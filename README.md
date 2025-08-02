[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20022136)
# Gestion de Inventario

Crear una función que permita gestionar el inventario de una tienda pequeña. La función debe registrar ventas de productos, actualizar las cantidades disponibles y calcular el índice de rotación del inventario.

Los productos, sus cantidades y el historial de ventas se almacenan en un archivo de texto.

Finalmente, la función debe **imprimir** el índice de rotación del inventario, que se define como:

`total_productos_vendidos / productos_diferentes_vendidos`

Donde:

- `total_productos_vendidos`: Es la cantidad total de productos vendidos (sumando todas las unidades)
- `productos_diferentes_vendidos`: Es la cantidad de productos diferentes que se vendieron

### Definición de la función

```python
def vender_productos(ruta, cantidad):
  ...
```

Donde:

- `ruta`: Es el nombre del archivo donde se almacena el inventario y el historial de ventas
- `cantidad`: Es la cantidad de productos diferentes que se van a vender en esta transacción

### Formato del archivo

El archivo almacena tanto el inventario como el historial de ventas:

`codigo_producto: cantidad_disponible`

Para diferenciar entre inventario y ventas históricas:

- Códigos positivos: Representan productos del inventario
- Códigos negativos: Representan el historial de ventas acumuladas

Por ejemplo:

```
1234: 50
5678: 23
9012: 105
-1234: 15
-5678: 7
```

En este ejemplo:

- El producto 1234 tiene 50 unidades disponibles y ha vendido 15 unidades históricamente
- El producto 5678 tiene 23 unidades disponibles y ha vendido 7 unidades históricamente

### Requerimientos

- Si la `cantidad` es menor o igual a cero, se debe imprimir un mensaje por pantalla indicando que la cantidad debe ser positiva.

- Si el archivo indicado por la `ruta` no existe, debe crearse con 10 productos iniciales (representados por los códigos `[1000-1009]`, cada uno con 100 unidades).

- Para cada venta, se debe elegir al azar un producto del inventario actual, y venderse entre 1 y 5 unidades, también al azar.

- Si un producto no tuviese suficiente stock, se vende lo que queda disponible. (En este caso, se actualiza el inventario solo con los que efectivamente se vendieron y no con los que se quisieron vender originalmente).

- Los productos con cantidad 0 deben permanecer en el archivo.

- El índice de rotación debe considerar todas las ventas históricas (acumulativas)

### Ejemplos de uso

1. Si no existe `inventario.txt` y se ingresa una cantidad negativa:

```
vender_productos("inventario.txt", -2)
```

Se imprime un mensaje por pantalla indicando que `cantidad` debe ser positiva y se retorna automáticamente. (También es aceptable levantar una excepción tipo Exception).


2. Si no existe `inventario.txt`:


```
vender_productos("inventario.txt", 3)
```

a. Se generan las listas de Python con datos iniciales (códigos 1000-1009, 100 de stock c/u):

```python
try:
  ...
except FileNotFoundError:
  for i in range(10):
      productos.append(1000 + i)
      cantidades.append(100)
```

b. Se venden 3 productos diferentes. Supongamos que se venden:
- Producto 1002: 3 unidades
- Producto 1005: 1 unidad
- Producto 1002: 2 unidades (se repitió)

Como se vendieron 6 unidades de 2 productos diferentes, se imprime por pantalla:

`El índice de rotación es: 3.0`

El archivo `inventario.txt` almacena:

```
1000: 100
1001: 100
1002: 94
1003: 100
1004: 100
1005: 99
1006: 100
1007: 100
1008: 100
1009: 100
-1002: 5
-1005: 1
```

3. Si existe `inventario.txt` y se vuelve a llamar a la función:

`vender_productos("inventario.txt", 2)`

Se venden otros 2 productos diferentes más. Supongamos que son:

- Producto 1002: 4 unidades
- Producto 1007: 2 unidades

Como se vendieron 12 unidades de 3 productos diferentes (entre los dos llamados), se imprime por pantalla:

`El índice de rotación es: 4.0`

Y se actualiza el archivo `inventario.txt`:

```
1000: 100
1001: 100
1002: 91
1003: 100
1004: 100
1005: 99
1006: 100
1007: 98
1008: 100
1009: 100
-1002: 9
-1005: 1
-1007: 2
```