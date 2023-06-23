# One Line Python

**Do everything in just one line!**

Remember that arrays are your allies. Forget about using multiple lines of code and do everything within arrays. This way, you can have "lines" with greater complexity while accomplishing simple tasks.

## Introduction
Welcome to the One Line Python repository! Here, we explore the art of writing concise Python code by challenging ourselves to accomplish tasks within a single line of code. This repository aims to showcase creative and efficient solutions to various programming problems, all condensed into a single line.

## Rules

1. All code must be written in just one line, including any imported files (with exceptions for standard and external modules/libraries).
2. Do not use `;` as a line separator.
3. Do not use `exec()`.

Below, you'll find different concepts applied in a one-line format. Keep in mind that these solutions may not always be the most efficient or suitable for every scenario. They are specific solutions found for these particular cases.

# Variables

I have found some solutions for defining and modifying variables:

## Using the `list` data type.

Recommended when you only need to use a single variable.

**Syntax**
```py
[... for variable in [value]]
```

You can try adding more values, but it's generally not recommended.

### Modifying the value.

The solution I found to modify the variable value is unconventional but functional:

**Syntax**
```py
[variable.replace(variable, new_value) for variable in [value]]
```

## Using the `dict` data type.

Great when you need to use multiple variables.

**Syntax**
```py
[... for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

### Modifying the value.

Use the `.update` method to alter the variable values.

**Syntax**
```py
[variables.update({'variable_A': 'new value'}) for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

## Modifying global variables.

Similar to the previous method, we can update global variables to add our own variables. This method is more interesting as it allows us to use the variable as if it were defined conventionally.

**Syntax**
```py
[globals().update({'variable':'value'})]
```

### Modifying the value.

Since we cannot use `=` to change the value of our variable, we can use the same method presented for modifying `dict` variables.

**Syntax**
```py
[globals().update({'variable':'new_value'})]
```

# Conditions

This topic can be skipped if you are already accustomed to using `if-else` statements within arrays since there are no significant changes in the implementation.

A standalone `if` statement without the need for an `else` can be added after the `for` statement:

**Syntax**
```py
[for variable in [value] if condition]
```

If an `else` statement is needed, you can add the condition before the `for` statement:

**Syntax**
```py
[... if condition else ... for variable in [value] ]
```

If an `elif` statement is needed, you can add additional `if` statements within the `else` section:

**Syntax**
```py
[... if condition else (... if condition else ...)  for variable in [value] ]
```

> The parentheses are optional; they were added for better visualization.

## Sequence of if statements

There are various scenarios with different purposes. In a scenario where you need a sequence of `if` statements that return different values without using `else`, you can represent the `else` condition as `None`:

**Syntax**
```py
[[... if condition else None, ... if condition else None] for variable in [value] ]
```

The issue with using this approach is that `None` values are present in the array. If this is problematic, you can use `filter` with `list` to remove these `None` values:

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

The solution for one-line functions is to use `lambda`. There's no need to use `return`. All the methods for defining variables can be applied here.

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

# Modules

To import modules, we can use the same concepts for defining and using the `__import__` function. This way, we can import the module entirely:

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

To create a `while` loop, we need to use recursion:

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

Here's another example:

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

# Classes

The approach I thought of for creating a `class` is to use `lambda` and `SimpleNamespace`:

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

Please let me know if you need further clarification or assistance with anything else.