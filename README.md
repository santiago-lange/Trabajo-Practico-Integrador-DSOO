# Sistema de Control de Stock Gastronómico

Trabajo Práctico Integrador de **Desarrollo de Sistemas Orientado a Objetos (DSOO)** — IFTS N.º 9.

Aplicación de consola en **Python 3.10+**, con arquitectura de tres capas y almacenamiento local mediante **SQLite**. No requiere dependencias externas.

## Ejecución

Desde la carpeta del repositorio:

```bash
python3 main.py
```

La primera ejecución crea automáticamente `stock.db` con tres productos:
- Empanadas: 50 unidades (código 1).
- Medialunas: 30 unidades (código 2).
- Chipá: 20 unidades (código 3).

En las siguientes ejecuciones se recuperan los valores guardados.

## Funcionalidades

1. Mostrar inventario.
2. Agregar stock a un producto.
3. Quitar stock (sin permitir cantidades negativas).
4. Registrar un producto con código único.
5. Eliminar un producto, previa confirmación.
6. Buscar un producto por código.
7. Poner el stock de un producto en cero, previa confirmación.
0. Salir.

Antes de agregar o quitar stock, registrar o eliminar productos y poner stock en cero, la consola muestra el inventario con sus códigos y cantidades disponibles. Se validan los valores ingresados y se rechazan códigos duplicados.

## Estructura del proyecto

```text
main.py
presentacion/
  consola.py
negocio/
  modelos.py
  servicio.py
datos/
  repositorio.py
test_stock.py
```

- **Presentación:** menú y entrada/salida de consola.
- **Negocio:** clases `Producto`, `Inventario` y `ServicioStock`; reglas de stock.
- **Datos:** `RepositorioSQLite`, que conserva el inventario en `stock.db`.

## Pruebas

```bash
python3 -m unittest -v test_stock.py
```

Las pruebas utilizan una base temporal independiente de `stock.db`, de modo que no alteran el inventario del usuario.

## Demostración opcional

```bash
python3 main.py --demo
```

**Atención:** la demostración modifica el stock persistido en `stock.db`.

## Alcance

El sistema conserva el estado actual del inventario; no lleva un historial de movimientos. Está pensado como aplicación local sencilla para demostrar programación orientada a objetos, separación en capas y persistencia de datos.
