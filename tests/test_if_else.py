def test_if():
    # Single if.
    assert ['Yes' for variable in ['value'] if variable == 'value'][0] == 'Yes'

def test_if_else():
    # If else.
    assert ['Yes' if variable == 'value' else 'No' for variable in ['new value']][0] == 'No'

def test_elif():
    # Elif.
    # variable = 5
    # if variable >= 10: print('Greater than or equal to 10')
    # elif variable >= 5: print('Greater than or equal to 5')
    # else: print('Less than 5.')
    assert ['Greater than or equal to 10' if variable >= 10 else 'Greater than or equal to 5' if variable >= 5 else 'Less than 5.' for variable in [5]][0] == 'Greater than or equal to 5'

def test_multiples_ifs():
    # variable = 3
    # if variable > 10: print('Greater than 10.')
    # if variable <= 10: print('Less than or equal to 10')
    # if variable <= 5: print('Less than or equal to 5')
    # if variable >= 1 and variable <= 5: print('Greater than or equal to 1')

    # Option 1 (array containing "None").
    assert [['Greater than 10.' if variable > 10 else None, 'Less than or equal to 10' if variable <= 10 else None, 'Less than or equal to 5' if variable <= 5 else None, 'Greater or equal to 1' if variable >= 1 and variable <= 5 else None] for variable in [3]][0] == [None, 'Less than or equal to 10', 'Less than or equal to 5', 'Greater or equal to 1']
    
    # Option 2 (set without "None").
    assert [{'Greater than 10.' if variable > 10 else None, 'Less than or equal to 10' if variable <= 10 else None, 'Less than or equal to 5' if variable <= 5 else None, 'Greater or equal to 1' if variable >= 1 and variable <= 5 else None}.difference({None}) for variable in [3]][0] == {'Greater or equal to 1', 'Less than or equal to 10', 'Less than or equal to 5'}