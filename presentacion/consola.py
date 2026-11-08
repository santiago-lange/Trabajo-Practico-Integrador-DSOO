"""Capa de presentación: interfaz interactiva por consola."""


def leer_entero(mensaje: str, minimo: int = 0) -> int:
    """Solicita un número entero válido, sin trasladar validaciones de negocio."""
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("Error: ingresá un número entero.")
            continue
        if numero < minimo:
            print(f"Error: ingresá un número mayor o igual a {minimo}.")
            continue
        return numero


def mostrar_inventario(servicio) -> None:
    lineas = servicio.mostrar_productos()
    print("\n--- INVENTARIO ---")
    print("\n".join(lineas) if lineas else "No hay productos registrados.")


def ejecutar_consola(servicio) -> None:
    """Ejecuta el menú hasta que el usuario elige salir."""
    while True:
        print("\n=== CONTROL DE STOCK GASTRONÓMICO ===")
        print("1. Ver inventario")
        print("2. Agregar stock")
        print("3. Quitar stock")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Buscar producto")
        print("7. Poner stock en cero")
        print("0. Salir")
        opcion = input("Elegí una opción: ").strip()
        try:
            if opcion == "1":
                mostrar_inventario(servicio)
            elif opcion in ("2", "3"):
                mostrar_inventario(servicio)
                codigo = leer_entero("Código del producto: ", 1)
                cantidad = leer_entero("Cantidad: ", 1)
                if opcion == "2":
                    servicio.agregar_stock(codigo, cantidad)
                else:
                    servicio.quitar_stock(codigo, cantidad)
                print("Stock actualizado correctamente.")
                print(servicio.buscar_producto(codigo))
            elif opcion == "4":
                print("\nCódigos existentes (elegí uno que no esté utilizado):")
                mostrar_inventario(servicio)
                codigo = leer_entero("Código nuevo: ", 1)
                nombre = input("Nombre del producto: ").strip()
                stock = leer_entero("Stock inicial: ", 0)
                servicio.agregar_producto(codigo, nombre, stock)
                print("Producto agregado correctamente.")
                mostrar_inventario(servicio)
            elif opcion == "5":
                mostrar_inventario(servicio)
                codigo = leer_entero("Código del producto a eliminar: ", 1)
                print(servicio.buscar_producto(codigo))
                confirmacion = input("¿Confirmás la eliminación? (s/n): ").strip().lower()
                if confirmacion == "s":
                    servicio.eliminar_producto(codigo)
                    print("Producto eliminado.")
                    mostrar_inventario(servicio)
                else:
                    print("Operación cancelada.")
            elif opcion == "6":
                codigo = leer_entero("Código del producto: ", 1)
                print(servicio.buscar_producto(codigo))
            elif opcion == "7":
                mostrar_inventario(servicio)
                codigo = leer_entero("Código del producto: ", 1)
                print(servicio.buscar_producto(codigo))
                confirmacion = input("¿Confirmás poner el stock en 0? (s/n): ").strip().lower()
                if confirmacion == "s":
                    servicio.poner_stock_en_cero(codigo)
                    print("Stock actualizado a 0. El producto sigue registrado.")
                    print(servicio.buscar_producto(codigo))
                else:
                    print("Operación cancelada.")
            elif opcion == "0":
                print("Hasta luego. Los cambios quedaron guardados.")
                break
            else:
                print("Opción no válida. Intentá nuevamente.")
        except ValueError as error:
            print(f"No se pudo realizar la operación: {error}")


def ejecutar_demostracion(servicio) -> None:
    """Demostración opcional para pruebas manuales (modifica el stock)."""
    mostrar_inventario(servicio)
    servicio.quitar_stock(1, 10)
    servicio.agregar_stock(2, 15)
    mostrar_inventario(servicio)
    try:
        servicio.quitar_stock(3, 100)
    except ValueError as error:
        print(f"Validación comprobada: {error}")
