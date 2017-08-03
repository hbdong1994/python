number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)

print(list(less_than_zero))


def less_zero(i):
    if i < 0:
        return True
    else:
        return False


def more_zero(i):
    if i > 0:
        return True
    else:
        return False

funcs = [more_zero]


for i in number_list:
    print(i)
    v = filter(lambda x: x(i), funcs)   # filter 是从集合 funcs中 筛选符合条件的值 作为list
    print(list(v))
