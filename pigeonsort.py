def pigeonsort(values):
    # size of range of values in the list (ie, number of pigeonholes we need)
    _min = min(values)
    _max = max(values)
    _range = _max - _min + 1

    # pigeonholes
    '''holes = [0 for i in range(_range)]'''
    holes = [0] * _range

    # populate the holes
    for x in values:
        holes[x - _min] += 1

    # new sorted list, putting elements back to save space
    i = 0
    for count in range(_range):
        while holes[count] > 0:
        #copy all elements from each hole
            holes[count] -= 1
            values[i] = count + _min
            i += 1
            
    return values
