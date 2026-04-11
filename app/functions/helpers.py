

def read_file_txt(path_file: str, encoding: str = "utf-8") -> list:
    """Función para leer un archivo de texto y devolver una lista de líneas.
    
    Args:
        path_file (str): Ruta del archivo de texto a leer.
        encoding (str): Codificación del archivo. Por defecto es "utf-8".

    Returns:
        list: Lista de líneas del archivo de texto.
    """

    with open(path_file, encoding=encoding) as f:
        lines = [line.strip() for line in f]
    return lines
