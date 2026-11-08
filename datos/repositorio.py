"""Capa de datos: persistencia local mediante SQLite."""
import sqlite3
from pathlib import Path


class RepositorioSQLite:
    def __init__(self, ruta: str | Path = "stock.db"):
        self.__ruta = str(ruta)
        with sqlite3.connect(self.__ruta) as conexion:
            existia = conexion.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='productos'"
            ).fetchone() is not None
            conexion.execute("""CREATE TABLE IF NOT EXISTS productos (
                codigo INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                stock INTEGER NOT NULL CHECK (stock >= 0)
            )""")
            if not existia:
                conexion.executemany(
                    "INSERT INTO productos (codigo, nombre, stock) VALUES (?, ?, ?)",
                    [(1, "Empanadas", 50), (2, "Medialunas", 30), (3, "Chipá", 20)],
                )

    def cargar(self) -> list[tuple[int, str, int]]:
        with sqlite3.connect(self.__ruta) as conexion:
            return conexion.execute(
                "SELECT codigo, nombre, stock FROM productos ORDER BY codigo"
            ).fetchall()

    def guardar(self, registros: list[tuple[int, str, int]]) -> None:
        # Reemplaza el conjunto de registros en una transacción.
        with sqlite3.connect(self.__ruta) as conexion:
            conexion.execute("DELETE FROM productos")
            conexion.executemany(
                "INSERT INTO productos (codigo, nombre, stock) VALUES (?, ?, ?)",
                registros,
            )
