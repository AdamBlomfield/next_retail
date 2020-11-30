def items_starting_with_string(_list, _string):
    '''Return items in list which begin with string'''
    return [i for i in _list if i.startswith(_string)]

def items_containing_string(_list, _string):
    '''Return items in list with the string'''
    return [i for i in _list if _string in i]

