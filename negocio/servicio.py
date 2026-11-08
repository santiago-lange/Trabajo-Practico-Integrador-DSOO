"""Coordina inventario y repositorio: presentación no accede directamente a datos."""
from negocio.modelos import Inventario, Producto


class ServicioStock:
    def __init__(self, repositorio):
        self.__repositorio = repositorio
        self.__inventario = Inventario()
        for codigo, nombre, stock in repositorio.cargar():
            self.__inventario.agregar_producto(Producto(codigo, nombre, stock))

    def __guardar(self) -> None:
        registros = [
            (p.codigo, p.nombre, p.stock)
            for p in self.__inventario.obtener_productos()
        ]
        self.__repositorio.guardar(registros)

    def mostrar_productos(self) -> list[str]:
        return self.__inventario.mostrar_productos()

    def agregar_stock(self, codigo: int, cantidad: int) -> None:
        producto = self.__obtener_producto(codigo)
        producto.agregar_stock(cantidad)
        self.__guardar()

    def quitar_stock(self, codigo: int, cantidad: int) -> None:
        producto = self.__obtener_producto(codigo)
        producto.quitar_stock(cantidad)
        self.__guardar()

    def poner_stock_en_cero(self, codigo: int) -> None:
        producto = self.__obtener_producto(codigo)
        producto.poner_stock_en_cero()
        self.__guardar()

    def agregar_producto(self, codigo: int, nombre: str, stock: int) -> None:
        self.__inventario.agregar_producto(Producto(codigo, nombre, stock))
        self.__guardar()

    def eliminar_producto(self, codigo: int) -> None:
        self.__inventario.eliminar_producto(codigo)
        self.__guardar()

    def buscar_producto(self, codigo: int) -> str:
        return self.__obtener_producto(codigo).mostrar_informacion()

    def __obtener_producto(self, codigo: int) -> Producto:
        producto = self.__inventario.buscar_producto(codigo)
        if producto is None:
            raise ValueError("El producto no existe.")
        return producto
