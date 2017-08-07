import inspect

mytuple = 1, 2, 3
mylist = [1, 2, 3]
print(dir(mytuple))
print(type(mytuple), type(mylist))
print(inspect.getmembers(mytuple))

mylist = [i ** 2 for i in range(10)]  # list 推导式
print(mylist)


mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {    # dict推导式
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

print(mcase_frequency)

mdict = {v: k for k, v in {'dean': 1, 'sean':2, 'poe': 3, 'lory': 4}.items()}
print(mdict)
