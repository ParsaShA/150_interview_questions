def remove_element(lst: list, val: int):
    x1 = [elm for elm in lst if elm != val]
    x2 = ['_' for _ in range(val)]
    k = len(x1)
    return k, x1+x2


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], val=2))
# Result = (5, [0, 1, 3, 0, 4, '_', '_'])
