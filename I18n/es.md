![One Line Python](../imgs/banner.png)

---

<a href="./index.md"><img src="../imgs/lang.gif" width=40% align="right"></a>

¡Olvida el uso de múltiples líneas en tu código! Compacta todo y realiza todo en tan solo una línea. Los arrays son tus aliados, te permiten realizar todas las tareas que solías hacer antes, ahora en una sola línea.

## Introducción
¡Bienvenido al repositorio de One Line Python! Aquí exploramos el arte de escribir código Python conciso desafiándonos a nosotros mismos a realizar tareas en tan solo una línea de código. Este repositorio tiene como objetivo mostrar soluciones creativas y eficientes a varios problemas de programación, todo en una sola línea.

# Tabla de contenido

- [Tabla de contenido](#tabla-de-contenido)
  - [Reglas](#reglas)
- [Conceptos de código](#conceptos-de-código)
  - [Variables](#variables)
    - [Usando el tipo de dato `list`.](#usando-el-tipo-de-dato-list)
      - [Modificando el valor.](#modificando-el-valor)
    - [Usando el tipo de dato `dict`.](#usando-el-tipo-de-dato-dict)
      - [Modificando el valor.](#modificando-el-valor-1)
    - [Modificando variables globales.](#modificando-variables-globales)
      - [Modificando el valor.](#modificando-el-valor-2)
  - [Condiciones](#condiciones)
    - [Secuencia de declaraciones `if`](#secuencia-de-declaraciones-if)
  - [Funciones](#funciones)
  - [Módulos](#módulos)
  - [Bucle While](#bucle-while)
  - [Clases](#clases)
- [Contribuir](#contribuir)
- [Licencia](#licencia)


## Reglas

1. Todo el código debe estar escrito en una sola línea, incluidos los archivos importados (con excepciones para los módulos/bibliotecas estándar y externos).
2. No utilices `;` como separador de líneas.
3. No utilices `exec()`.

A continuación, encontrarás diferentes conceptos aplicados en formato de una sola línea. Ten en cuenta que estas soluciones no siempre serán las más eficientes o adecuadas para cada escenario. Son soluciones específicas encontradas para estos casos particulares.

# Conceptos de código

## Variables

He encontrado algunas soluciones para definir y modificar variables:

### Usando el tipo de dato `list`.

Recomendado cuando solo necesitas usar una sola variable.

**Sintaxis**
```py
[... for variable in [valor]]
```

Puedes intentar agregar más valores, pero generalmente no se recomienda.

#### Modificando el valor.

La solución que encontré para modificar el valor de la variable es poco convencional pero funcional:

**Sintaxis**
```py
[variable.replace(variable, nuevo_valor) for variable in [valor]]
```

### Usando el tipo de dato `dict`.

Excelente cuando necesitas usar múltiples variables.

**Sintaxis**
```py
[... for variables in [{'variable_A': 'valor', 'variable_B': 'valor', ...}]]
```

#### Modificando el valor.

Utiliza el método `.update` para modificar los valores de las variables.

**Sintaxis**
```py
[variables.update({'variable_A': 'nuevo valor'}) for variables in [{'variable_A': 'valor', 'variable_B': 'valor', ...}]]
```

### Modificando variables globales.

Similar al método anterior, podemos actualizar variables globales para agregar nuestras propias variables. Este método es más interesante, ya que nos permite usar la variable como si estuviera definida convencionalmente.

**Sintaxis**
```py
[globals().update({'variable':'valor'})]
```

#### Modificando el valor.

Dado que no podemos usar `=` para cambiar el valor de nuestra variable, podemos utilizar el mismo método presentado para modificar variables `dict`.

**Sintaxis**
```py
[globals().update({'variable':'nuevo_valor'})]
```

## Condiciones

Este tema se puede omitir si ya estás acostumbrado a usar declaraciones `if-else` dentro de arrays, ya que no hay cambios significativos en la implementación.

Una declaración `if` independiente sin la necesidad de un `else` se puede agregar después de la declaración `for`:

**Sintaxis**
```py
[for variable in [valor] if condición]
```

Si se necesita una declaración `else`, puedes agregar la condición antes

 de la declaración `for`:

**Sintaxis**
```py
[... if condición else ... for variable in [valor] ]
```

Si se necesita una declaración `elif`, puedes agregar declaraciones `if` adicionales dentro de la sección `else`:

**Sintaxis**
```py
[... if condición else (... if condición else ...)  for variable in [valor] ]
```

> Los paréntesis son opcionales, se agregaron para una mejor visualización.

### Secuencia de declaraciones `if`

Existen diversos escenarios con diferentes propósitos. En un escenario donde se necesita una secuencia de declaraciones `if` que devuelvan diferentes valores sin usar `else`, puedes representar la condición `else` como `None`:

**Sintaxis**
```py
[[... if condición else None, ... if condición else None] for variable in [valor] ]
```

El problema de usar este enfoque es que los valores `None` están presentes en el array. Si esto es problemático, puedes usar `filter` con `list` para eliminar estos valores `None`:

**Sintaxis**
```py
[list(filter(lambda resultado_condición: resultado_condición != None, [... if condición else None, ... if condición else None])) for variable in [valor] ]
```

**Ejemplo**

```py
[list(filter(lambda resultado_condición: resultado_condición != None, ['Mayor que 10' if número > 10 else None, 'Mayor que 20' if número > 20 else None])) for número in [11]]
```

**Equivalente a**
```py
número = 40
if número > 10: print('Mayor que 10')
if número > 20: print('Mayor que 20')
```

## Funciones

La solución para funciones de una sola línea es usar `lambda`. No es necesario utilizar `return`. Todos los métodos para definir variables se pueden aplicar aquí.

**Sintaxis** *(list)*
```py
[función() for función in [lambda parámetro: ...]]
```
**Sintaxis** *(dict)*
```py
[variables['función']() for variables in [{'función': lambda parámetro: ...}]]
```
**Sintaxis** *(global)*
```py
[globals().update({'función': lambda parámetro: ...})]
```

**Ejemplo**

```py
[[impar(número) for número in [2,11,5]] for impar in [lambda número: "Es par" if número % 2 == 0 else "Es impar"]]
```

**Equivalente a**
```py
def impar(número):
    if número % 2 == 0: return "Es par"
    return "Es impar"

impar(2) # Es par
impar(11) # Es impar
impar(5) # Es impar
```

## Módulos

Para importar módulos, podemos usar los mismos conceptos para definir y utilizar la función `__import__`. De esta manera, podemos importar el módulo por completo:

**Sintaxis**
```py
[... for módulo in [__import__('nombre_módulo')]]
```

**Ejemplo**

```py
[os.listdir('./') for os in [__import__('os')]]
```

**Equivalente a**

```py
import os
os.listdir('./')
```

## Bucle While

Para crear un bucle `

while` de una sola línea, simplemente colocamos la condición después del bucle `while`:

**Sintaxis**
```py
[while condición: ... for variable in [valor]]
```

**Ejemplo**

```py
[[i for i in range(5)] for _ in [None] while i < 3]
```

**Equivalente a**

```py
i = 0
while i < 3:
    print(i)
    i += 1
```

## Clases

Si quieres definir una clase de una sola línea, puedes usar la función `type` para hacerlo:

**Sintaxis**
```py
[type('NombreClase', (ClaseBase,), {'método': lambda self: ...})]
```

**Ejemplo**

```py
[type('Persona', (), {'saludar': lambda self: print('Hola')})]
```

**Equivalente a**

```py
class Persona:
    def saludar(self):
        print('Hola')
```

# Contribuir

¡Se agradecen mucho las contribuciones al repositorio de One Line Python! Si tienes una solución creativa de una sola línea para compartir o quieres mejorar el código existente, sigue estos pasos:

1. Haz un *fork* del repositorio.
2. Crea una nueva rama para tu función o corrección de errores.
3. Haz *commit* de tus cambios con mensajes claros y concisos.
4. Haz *push* de tus cambios a tu repositorio *forked*.
5. Envía una solicitud de extracción (*pull request*) describiendo en detalle tus cambios.

# Licencia

El repositorio de One Line Python está bajo la Licencia MIT.