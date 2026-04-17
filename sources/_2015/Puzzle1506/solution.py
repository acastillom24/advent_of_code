"""
--- Día 6: Probablemente un peligro de incendio ---

Como tus vecinos siguen derrotándote en el concurso de decoración navideña de casas año tras año, 
has decidido desplegar un millón de luces en una cuadrícula de 1000x1000.

Además, como este año has sido especialmente amable, Papá Noel te ha enviado por correo las 
instrucciones para desplegar la configuración de iluminación ideal.

Las luces de tu cuadrícula están numeradas del 0 al 999 en cada dirección; las luces de cada 
esquina están en 0,0, 0,999, 999,999 y 999,0. Las instrucciones incluyen si encender, apagar o 
alternar varios rangos inclusivos dados como pares de coordenadas. Cada par de coordenadas 
representa esquinas opuestas de un rectángulo, inclusive; un par de coordenadas como 0,0 a 2,2 
por lo tanto se refiere a 9 luces en un cuadrado de 3x3. Todas las luces empiezan apagadas.

Para vencer a tus vecinos este año, lo único que tienes que hacer es colocar las luces siguiendo 
las instrucciones que te ha enviado Papá Noel en orden.

Por ejemplo
encender de 0,0 a 999,999 encendería (o dejaría encendidas) todas las luces.
alternar 0,0 a 999,0 alternaría la primera línea de 1000 luces, apagando las que estuvieran encendidas y encendiendo las que estuvieran apagadas.
apagar de 499,499 a 500,500 apagaría (o dejaría apagadas) las cuatro luces del medio.

Después de seguir las instrucciones, ¿cuántas luces están encendidas?
"""

# %% Carga de las bibliotecas
import numpy as np
import re

# %% Carga de los datos
PATH_FILE = "input.txt"
with open(PATH_FILE) as f:
    lines = f.readlines()
f.close()

# %% Desarrollo
grid = np.full((1000,1000), False)

for row in lines:
    coord = [int(idx) for idx in re.findall(r'\d+', row)]
    if coord:
        x1, y1, x2, y2 = coord
        if row.startswith("turn off"):
            grid[x1:x2+1, y1:y2+1] = False
        elif row.startswith("turn on"):
            grid[x1:x2+1, y1:y2+1] = True
        elif row.startswith("toggle"):
            grid[x1:x2+1, y1:y2+1] = ~grid[x1:x2+1, y1:y2+1]

(grid==True).sum()            

# %%
"""
--- Segunda parte.
Acabas de terminar de implementar tu patrón de luces ganador cuando te das cuenta de que has traducido mal el mensaje de Papá Noel del antiguo élfico nórdico.

La rejilla de luces que compraste en realidad tiene controles de brillo individuales; cada luz puede tener un brillo de cero o más. Todas las luces empiezan en cero.

La frase encender en realidad significa que debes aumentar el brillo de esas luces en 1.

La frase apagar en realidad significa que usted debe disminuir el brillo de esas luces en 1, a un mínimo de cero.

La frase alternar en realidad significa que debes aumentar la luminosidad de esas luces en 2.

¿Cuál es la luminosidad total de todas las luces combinadas después de seguir las instrucciones de Papá Noel?

Por ejemplo:

encender 0,0 hasta 0,0 aumentaría el brillo total en 1.
encender 0,0 hasta 999,999 aumentaría el brillo total en 2000000.
"""

grid = np.zeros((1000,1000))

for row in lines:
    coord = [int(idx) for idx in re.findall(r'\d+', row)]
    if coord:
        x1, y1, x2, y2 = coord
        if row.startswith("turn off"):
            grid[x1:x2+1, y1:y2+1] -= 1
            grid = grid.clip(0)
        elif row.startswith("turn on"):
            grid[x1:x2+1, y1:y2+1] += 1
        elif row.startswith("toggle"):
            grid[x1:x2+1, y1:y2+1] += 2

int(np.sum(grid))

# %%
