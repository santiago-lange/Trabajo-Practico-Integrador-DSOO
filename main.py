"""Punto de entrada del sistema de stock gastronómico."""
from pathlib import Path
import sys

from datos.repositorio import RepositorioSQLite
from negocio.servicio import ServicioStock
from presentacion.consola import ejecutar_consola, ejecutar_demostracion


def main() -> None:
    repositorio = RepositorioSQLite(Path(__file__).with_name("stock.db"))
    servicio = ServicioStock(repositorio)
    try:
        if "--demo" in sys.argv:
            ejecutar_demostracion(servicio)
        else:
            ejecutar_consola(servicio)
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalizado. Los cambios previos quedaron guardados.")


if __name__ == "__main__":
    main()
