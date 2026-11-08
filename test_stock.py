"""Pruebas automáticas de las reglas y persistencia del sistema."""
import tempfile
import unittest
from pathlib import Path
from datos.repositorio import RepositorioSQLite
from negocio.modelos import Producto
from negocio.servicio import ServicioStock


class PruebasStock(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.ruta = Path(self.temporal.name) / "prueba.db"
        self.servicio = ServicioStock(RepositorioSQLite(self.ruta))

    def tearDown(self):
        self.temporal.cleanup()

    def test_productos_iniciales(self):
        self.assertEqual(len(self.servicio.mostrar_productos()), 3)
        self.assertIn("Empanadas", self.servicio.buscar_producto(1))

    def test_agregar_y_quitar_stock(self):
        self.servicio.agregar_stock(1, 10)
        self.assertIn("Stock: 60", self.servicio.buscar_producto(1))
        self.servicio.quitar_stock(1, 15)
        self.assertIn("Stock: 45", self.servicio.buscar_producto(1))

    def test_no_permitir_stock_negativo(self):
        with self.assertRaises(ValueError):
            self.servicio.quitar_stock(3, 100)
        self.assertIn("Stock: 20", self.servicio.buscar_producto(3))

    def test_no_permitir_cantidades_invalidas(self):
        with self.assertRaises(ValueError):
            self.servicio.agregar_stock(1, 0)
        with self.assertRaises(ValueError):
            self.servicio.quitar_stock(1, -1)

    def test_alta_y_baja_de_productos(self):
        self.servicio.agregar_producto(4, "Alfajores", 8)
        self.assertIn("Alfajores", self.servicio.buscar_producto(4))
        self.servicio.eliminar_producto(4)
        with self.assertRaises(ValueError):
            self.servicio.buscar_producto(4)

    def test_codigo_repetido(self):
        with self.assertRaises(ValueError):
            self.servicio.agregar_producto(1, "Otro", 2)

    def test_poner_stock_en_cero(self):
        self.servicio.poner_stock_en_cero(2)
        self.assertIn("Stock: 0", self.servicio.buscar_producto(2))

    def test_persistencia_entre_ejecuciones(self):
        self.servicio.quitar_stock(1, 7)
        nuevo_servicio = ServicioStock(RepositorioSQLite(self.ruta))
        self.assertIn("Stock: 43", nuevo_servicio.buscar_producto(1))


if __name__ == "__main__":
    unittest.main()
