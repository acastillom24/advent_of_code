import os
from typing import Optional
import sys


def read_input_txt(
    year: int,
    day: int,
    transformer: str,
    path_file: Optional[str] = None,
    encoding: str = "utf-8",
) -> list:
    """Función para leer un archivo de texto y devolver una lista de líneas.

    Args:
        path_file (str): Ruta del archivo de texto a leer.
        year (int): Año para el cual leer el archivo.
        day (int): Número del día para el cual leer el archivo.
        transformer (str): Función para transformar cada línea.
        encoding (str): Codificación del archivo. Por defecto es "utf-8".

    Returns:
        list: Lista de líneas del archivo de texto.
    """

    if day < 1 or day > 25:
        raise ValueError("El número del día debe estar entre 1 y 25.")
    else:
        if path_file is None:
            if day < 10:
                day = f"0{day}"
            path_file = os.path.join("inputs", f"Puzzle{year}{day}.txt")
        else:
            raise ValueError("La ruta del archivo no es válida.")

    try:
        with open(path_file, encoding=encoding) as f:
            return [transformer(line.strip()) for line in f]
    except FileNotFoundError as e:
        print(e)


def read_stdin(transformer: str) -> Optional[list]:
    """Función para leer datos desde la entrada estándar (stdin) y devolver una lista de líneas.
    Args:
        transformer (str): Función para transformar cada línea.
    Returns:
        list: Lista de líneas leídas desde la entrada estándar.
    """
    lines = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            lines.append(transformer(line.strip()))
        except EOFError:
            break
    return lines if lines else None
