# ADVENTOFCODE

Exercise solution from [adventofcode.com](adventofcode.com)

## Función `read_input_txt`

Argumentos que recibe:

- year (int): Año para el cual leer el archivo.
- day (int): Número del día para el cual leer el archivo.
- transformer (str): Función para transformar cada línea.
- path_file Optional[str]: Ruta del archivo de texto a leer.
- encoding (str): Codificación del archivo. Por defecto es "utf-8".

Ejemplo:

- Leer los datos del puzzle 7 del año 2015

```bash
def transformer(line):
    s, e = line.split(" -> ")
    return (s, e)

read_input_txt(15, 7, transformer)
```

## Ejecutar Puzzle 7

**En cada carpeta del puzzle se encuentra un README con el problema descrito**

```bash
puzzle = Puzzle1507()
wires = puzzle.solveA(connections)
signal_overrides = {}
signal_overrides["b"] = wires["a"]
wires = puzzle.solveB(connections, signal_overrides)
print(wires["a"]) 
```
