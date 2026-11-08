"""Objetos del dominio y sus reglas de stock."""


class Producto:
    def __init__(self, codigo: int, nombre: str, stock: int):
        if type(codigo) is not int or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if type(stock) is not int or stock < 0:
            raise ValueError("El stock inicial debe ser un entero no negativo.")
        self.__codigo = codigo
        self.__nombre = nombre.strip()
        self.__stock = stock

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def stock(self) -> int:
        return self.__stock

    def agregar_stock(self, cantidad: int) -> None:
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        self.__stock += cantidad

    def quitar_stock(self, cantidad: int) -> None:
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        if cantidad > self.__stock:
            raise ValueError("No hay stock suficiente.")
        self.__stock -= cantidad

    def poner_stock_en_cero(self) -> None:
        """Deja el producto registrado, pero sin existencias."""
        self.__stock = 0

    def mostrar_informacion(self) -> str:
        return f"Código: {self.codigo} | Producto: {self.nombre} | Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.__productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos Producto.")
        if self.buscar_producto(producto.codigo) is not None:
            raise ValueError("Ya existe un producto con ese código.")
        self.__productos.append(producto)

    def eliminar_producto(self, codigo: int) -> None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("El producto no existe.")
        self.__productos.remove(producto)

    def buscar_producto(self, codigo: int) -> Producto | None:
        return next((p for p in self.__productos if p.codigo == codigo), None)

    def mostrar_productos(self) -> list[str]:
        return [p.mostrar_informacion() for p in self.__productos]

    def obtener_productos(self) -> tuple[Producto, ...]:
        return tuple(self.__productos)
