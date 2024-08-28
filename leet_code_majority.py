def f(x):
    return lst.count(x)


lst = [2, 2, 1, 1, 1, 2, 2]
n = len(lst) // 2
d = {x: f(x) for x in lst if f(x) > n}
print(*sorted(d, key=lambda x: d[x]))
