# variable = 3
# if variable > 10: print('Maior que 10.')
# if variable <= 10: print('Menor ou igual a 10')
# if variable <= 5: print('Menor ou igual a 5')
# if variable >= 1 and variable <= 5: print('Maior ou igual a 1')


# print([{'Greater than 10.' if variable > 10 else None, 'Less than or equal to 10' if variable <= 10 else None, 'Less than or equal to 5' if variable <= 5 else None, 'Greater or equal to 1' if variable >= 1 and variable <= 5 else None}.difference({None}) for variable in [3]])
# print([['Greater than 10.' if variable > 10 else None, 'Less than or equal to 10' if variable <= 10 else None, 'Less than or equal to 5' if variable <= 5 else None, 'Greater or equal to 1' if variable >= 1 and variable <= 5 else None] for variable in [3]][0])

# print([list(filter(lambda x: x != None, ['Greater than 10.' if variable > 10 else None, 'Less than or equal to 10' if variable <= 10 else None, 'Less than or equal to 5' if variable <= 5 else None, 'Greater or equal to 1' if variable >= 1 and variable <= 5 else None])) for variable in [3]][0])


# number = 40
# if number > 10: print('Maior que 10')
# if number > 20: print('Maior que 20')

# print([['Maior que 10' if number > 10 else None, 'Maior que 20' if number > 20 else None] for number in [11]])

# [while_loop(while_loop) for while_loop in [lambda cycle: [print('Hello World'), cycle(cycle)][1]]]

# print([globals().update({'size': lambda number: len(str(number))}), [size(number) for number in [1, 6, 10, 300, 1234]]])

# i = 0
# while i <= 5:
#     print(i)
#     i += 1
    
# [globals().update({'i':0}), [while_loop(while_loop) for while_loop in [lambda cycle: [[print(i), globals().update({'i':i+1})], cycle(cycle) if i <= 5 else None][1]]]]


print(
    [globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'Cat': lambda name: [_['methods']['__init__'](_['self']) for _ in [{'self': {'x':1}, 'methods': {'__init__': lambda self: print(self)}}]]}), Cat("tom")]
)

# print([globals().update({'importlib':__import__('importlib')}), globals().update({'os':importlib.import_module('os')}), globals().update({'listdir': getattr(os, 'listdir')}), dir(os)])