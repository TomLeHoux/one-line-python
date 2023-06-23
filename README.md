# One Line Python

Faça tudo em apenas uma linha!

Lembre-se que arrays são seus aliados, tudo o que você fazia antes com diversas linhas esqueça, faça tudo dentro de arrays, dessa forma você pode ter "linhas" com uma complexidade maior de fazer coisas simples.

# Regras

1. Todo o código deve ser escrito em apenas uma linha, isso também se aplica a outros arquivos importados (com exeções dos módulos/bibliotecas padrões e externas);
2. Não utillize `;` como separador de linhas;
3. Não utilize `exec()`.

Abaixo foram as formas que encontrei de aplicar diferentes conceitos em apenas uma linha, lembre-se que eles podem não ser os mais eficientes e nem podem funcionar para todos os cenários, essas foram as solições que achei para esses determinados casos.

# Variables

Encontrei algumas soluções para definir e alterar as variáveis:

## Usando o tipo de data `list`.

Recomendo quando você precisa utilizar apenas uma variável.

**Syntax**
```py
[... for variable in [value]]
```

Você pode tentar implementar mais valores, mas acredito não ser uma boa pratica.

### Mudando o valor.

A solução que encontrei para alterar o valor da variável é bem inusitada, porém funcional:

**Syntax**
```py
[variable.replace(variable, new_value) for variable in [value]]
```

## Usando o tipo de data `dict`.

Muito boa quando se precisa utilizar diversas variáveis.

**Syntax**
```py
[... for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

### Mudando o valor.

Utilize o método `.update` para alterar os valores das variáveis.

**Syntax**
```py
[variables.update({'variable_A': 'new value'}) for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

## Alterando as variáveis globais.

Semelhante ao método anterior podemos atualizar as variáveis globais para adicionarmos nossas variáveis. Esse método é mais interessante do que os outros pois podemos utilizar a variável normalmente como se tivessemos definido ela da forma convencional.

**Syntax**
```py
[globals().update({'variable':'value'})]
```


### Mudando o valor.

Como não podemos utilizar `=` para alterar o valor da nossa variável, podemos utilizar o mesmo método apresentado para alterar as "variáveis de `dict`".

**Syntax**
```py
[globals().update({'variable':'new_value'})]
```

# Condições

É tópico pode ser completamente pulado se você já estiver acostumado a utilizar `if else` dentro de arrays, pois não há alterações muito significantes na forma de implementar-las.

Um `if` sozinho sem a necessidade do `else` pode ser adicionado após o `for`: 

**Syntax**
```py
[for variable in [value] if condition]
```

Caso seja necessário adicionar um `else` você pode fazer isso adicionando a condição antes do `for`:

**Syntax**
```py
[... if condition else ... for variable in [value] ]
```

Se preciso de `elif` você pode fazer isso adicionando novos `ifs` dentro dos `else`:

**Syntax**
```py
[... if condition else (... if condition else ...)  for variable in [value] ]
```

> Os parênteses são opcionais, eles foram adicionados para ajudar na visualização.

## Sequencia de if

Existem diversos cenários e com finalidades diferentes, no cenário em que você precisa de uma sequencia de `if` que retornam valores diferentes, para não utilizar `else` coloquei como `None`:

**Syntax**
```py
[[... if condition else None, ... if condition else None] for variable in [value] ]
```

O problema de utilizar dessa forma é justamente o fato dos `None` estarem presente no array. Caso seja um problema podemos utilizar `filter` junto com `list` para removermos esses None:

**Syntax**
```py
[list(filter(lambda condition_result: condition_result != None, [... if condition else None, ... if condition else None])) for variable in [value] ]
```

**Example**

```py
[list(filter(lambda condition_result: condition_result != None, ['Greater than 10' if number > 10 else None, 'Greater than 20' if number > 20 else None])) for number in [11]]
```

**Equivalent to**
```py
number = 40
if number > 10: print('Greater than 10')
if number > 20: print('Greater than 20')
```

# Functions

A solução para funções em apenas uma linha é `lambda`. Não é necessário utilizar `return`. Todas as outras formas de definir variáveis podem ser aplicadas aqui.

**Syntax** *(list)*
```py
[function() for function in [lambda parameter: ...]]
```
**Syntax** *(dict)*
```py
[variables['function']() for variables in [{'function': lambda parameter: ...}]]
```
**Syntax** *(global)*
```py
[globals().update({'function': lambda parameter: ...})]
```

**Example**

```py
[[odd(number) for number in [2,11,5]] for odd in [lambda number: "Is even" if number % 2 == 0 else "Is odd"]]
```

**Equivalent to**
```py
def odd(number):
    if number % 2 == 0: return "Is even"
    return "Is odd"

odd(2) # Is even
odd(11) # Is odd
odd(5) # Is odd
```

# Modulos

Para importar modulos podemos utilizar os mesmos conceitos para definir e utilizar a função `__import__`, dessa forma importaremos o módulo completamente:

**Syntax**
```py
[... for module in [__import__('module_name')]]
```

**Example**

```py
[os.listdir('./') for os in [__import__('os')]]
```

**Equivalent to**

```py
import os
os.listdir('./')
```

# While Loop

Para criamos `while` precisamos utilizar recursão:

**Syntax**
```py
[while_loop(while_loop) for while_loop in [lambda cycle: [..., cycle(cycle) if condition else None][1]]]
```

**Example**

```py
[globals().update({'i':0}), [while_loop(while_loop) for while_loop in [lambda cycle: [[print(i), globals().update({'i':i+1})], cycle(cycle) if i <= 5 else None][1]]]]
```

**Equivalent to**

```py
i = 0
while i <= 5:
    print(i)
    i += 1
```

Veja outro exemplo abaixo:

**Example**

```py
[[while_loop(while_loop) for while_loop in [lambda cycle: [[print(odd(number)) for number in [int(input('Number: '))]], cycle(cycle)][1]]] for odd in [lambda number: "Is odd" if number % 2 == 0 else "Is even"]]
```

**Equivalent to**
```py
def odd(number):
    if number % 2 == 0: return "Is even"
    return "Is odd"

while True:
    number = int(input("Number: "))
    print(odd(number))
```

# `Class`

A forma com que eu pensei em solucionar a criação de `class` foi usando `lambda` e `SimpleNamespace`:

**Syntax**
```py
[globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'class_name': lambda parameters: [<init code>, SimpleNamespace(**{'method': lambda parameters: ...})][1]})]
```

**Example**
```py
[globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'Cat': lambda name: [print(f"Your cat's name is {name}."), SimpleNamespace(**{'meow': lambda: print(f'{name}: Meow!')})][1]}), Cat('Tom').meow()]
```

**Equivalent to**
```py
class Cat:
     def __init__(self, name) -> None:
         self.name = name
         print(f"Your cat's name is {self.name}.")
    
     def meow(self) -> None:
         print(f'{self.name}: Meow!')

Cat('Tom').meow()
```