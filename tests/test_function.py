def test_array_function():
    # Function as a array value.
    assert [size(numbers) for numbers in [1, 6, 10, 300, 1234] for size in [lambda number: len(str(number))]] == [1, 1, 2, 3, 4]

def test_dict_function():
    # Function in dict variables.
    assert [[vars['size'](numbers) for numbers in vars['numbers']] for vars in [{'size': lambda number: len(str(number)), 'numbers': [1, 6, 10, 300, 1234]}]][0] == [1, 1, 2, 3, 4]

def test_global_function():
    # Function in global variables.
    assert [globals().update({'size': lambda number: len(str(number))}), [size(number) for number in [1, 6, 10, 300, 1234]]][1] == [1, 1, 2, 3, 4]