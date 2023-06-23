def test_array_variable():
    # "For" single variable.
    assert [variable for variable in ['value']][0] == 'value'

def test_multiple_array_variables():
    # Different Scopes.
    assert [[variable_A+variable_B for variable_B in ['B']] for variable_A in ['A']][0][0] == "AB"

def test_dict_variables():
    # Dict variables.
    assert [vars['variable_A']+vars['variable_B'] for vars in [{'variable_A':'A', 'variable_B':'B'}]][0] == "AB"

def test_global_variables():
    # Global variables.
    [globals().update({key:value}) for key, value in {'variable_A':'A', 'variable_B':'B'}.items()]
    assert variable_A == 'A'
    assert variable_B == 'B'