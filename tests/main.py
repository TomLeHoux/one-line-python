# print('One Line Python')

# [print(variable) for variable in ['value'] ]

# # Definindo variáveis.

# var = 'value'; print(var)
# vars = {'first': 'first value', 'second': 'second value'}; print(vars['second'])
# first, second = 'first value', 'sencond value'; print(second)

# [print(var) for var in ['value']]
# [print(vars[0]) for vars in ['first', 'second']]
# [print(vars['second']) for vars in [{'first': 'first value', 'second': 'second value'}]]

# # Mudando variávies.

# vars = {'gato':'miau'}; [exec('vars["gato"] = "purr"'), print(vars['gato'])]
# [ [exec('variables["key"] = 1'), print(variables['key'])] for variables in [{'key':'value'}] ]

# # If else

# [[print(var) for var, value in vars.items() if value == 'moo'] for vars in [{'cat':'meow', 'dog':'bark', 'cow':'moo'}]]
# [print('A nice True') if var else print('A nice False') for var in [True]]

# # Elif

# [print('Menor que 1') if number < 1 else print('Maior que 1') if number < 5 else print('Maior que 5') if number < 10 else print('Maior que 10') for number in [0]]

# Function

# [[print(odd(value)) for odd in [lambda number: True if number % 2 == 0 else False ]] for value in [int(input('Number: '))]]

# While Loop.

# [while_loop(while_loop) for while_loop in [lambda again:[[[print(odd(value)), again(again)] for odd in [lambda number: True if number % 2 == 0 else False ]] for value in [int(input('Number: '))]]]]

# print(
#     [globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'Cat': lambda name: [print(locals()), SimpleNamespace(**{'miar': lambda: print(locals())})][1]}), Cat('Tom').miar()]
#     # [globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'Cat': lambda name: [print(f'O nome do seu gato é {name}.'), SimpleNamespace(**{'miar': lambda: print(f'{name}: Miau!')})][1]}), Cat('Tom').miar()]
# )

class Cat:
    def __init__(self, name) -> None:
        self.name = name
        print(f'O nome do seu gato é {self.name}.')
    
    def miar(self) -> None:
        print(f'{self.name}: Miau!')

Cat('Tom').miar()

[globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'Cat': lambda name: [print(f'O nome do seu gato é {name}.'), SimpleNamespace(**{'miar': lambda: print(f'{name}: Miau!')})][1]}), Cat('Tom').miar()]

# # Class
# class objeto:
#     def __init__(self, parametro) -> None:
#         self.parametro = parametro
#         print("Objeto")

#     def func(self) -> None:
#         print("Função", self.parametro)

# # x = objeto("Valor")
# # x.func()
# from types import SimpleNamespace
# line_obj = lambda parametro: [print(parametro), SimpleNamespace(**{"func": lambda: print("Função", parametro)})][1]
# x = line_obj("Valor")
# x.func()