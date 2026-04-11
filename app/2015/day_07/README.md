# --- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and [bitwise logic gates](https://en.wikipedia.org/wiki/Bitwise_operation)! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

- 123 -> x means that the signal 123 is provided to wire x.
- x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
- p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
- NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

```bash
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```

After it is run, these are the signals on the wires:

```bash
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
```

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

# Día 7: Se necesita algo de montaje

Este año, Papá Noel le ha traído al pequeño Bobby Tables un juego de cables y puertas lógicas. 
Por desgracia, el pequeño Bobby está un poco por debajo de la edad recomendada y necesita ayuda para montar el circuito.

Cada cable tiene un identificador (unas letras minúsculas) y puede transportar una señal de 16 bits (un número del 0 al 65535). 
Cada cable recibe una señal de una puerta, de otro cable o de algún valor específico. 
Cada cable sólo puede recibir una señal de una fuente, pero puede proporcionar su señal a múltiples destinos. 
Una puerta no proporciona ninguna señal hasta que todas sus entradas tienen una señal.

El manual de instrucciones incluido describe cómo conectar las piezas entre sí: 
x AND y -> z significa conectar los hilos x e y a una puerta AND y, a continuación, conectar su salida al hilo z.

Por ejemplo
    123 -> x significa que se proporciona la señal 123 al cable x.
    x AND y -> z significa que el bitwise AND de los hilos x e y se proporciona al hilo z.
    p LSHIFT 2 -> q significa que el valor del cable p se desplaza a la izquierda en 2 y luego se proporciona al cable q.
    NOT e -> f significa que el complemento a nivel de bits del valor del cable e se proporciona al cable f.

Otras puertas posibles son OR (bitwise OR) y RSHIFT (right-shift). 
Si, por alguna razón, desea emular el circuito en su lugar, casi todos los lenguajes de programación 
(por ejemplo, C, JavaScript o Python) proporcionan operadores para estas puertas.

Por ejemplo, aquí tienes un circuito sencillo:
    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i

Después de que se ejecuta, estas son las señales en los cables:
    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456

En el libro de instrucciones del kit del pequeño Bobby (proporcionado como entrada de tu puzzle), 
¿qué señal se proporciona en última instancia para cablear un?
