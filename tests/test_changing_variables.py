def test_array_variable():
    assert [variable.replace(variable, 'new value') for variable in ['value']][0] == 'new value'

def test_array_value_variable():
    # Changing if value is array.
    assert [[variable.clear(), variable.append('new value'), variable[0]] for variable in [['value']]][0][2] == 'new value'

def test_dict_variables():
    assert [[vars.update({'variable_A': 'new A'}), vars] for vars in [{'variable_A':'A', 'variable_B':'B'}]][0][1]['variable_A'] == 'new A'

def test_global_variables():
    # Global variables.
    [[globals().update({key:value}) for key, value in {'variable_A':'A', 'variable_B':'B'}.items()], [globals().update({'variable_A':'new A'})]]
    assert variable_A == 'new A'
    assert variable_B == 'B'