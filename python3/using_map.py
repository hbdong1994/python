items = [1, 2, 3, 4, 5]
squared = []

squared = list(map(lambda i: i**3, items))  # i**n 就是i的n次方
print(squared)


def func_map(x):
    return x * x

use_func = list(map(lambda i: i**4, items))  # 使用lambda函数要好 少定义函数变量  类似于匿名函数
print(use_func)


def multiply(i):
    return i*i


def add(i):
    return i+1


funcs = [multiply, add]   #如果是作为函数 则不能是字符串
for i in range(5):
    v_map = map(lambda x: x(i), funcs)   # funcs 是函数列表  类似于php中变量名函数 php: $func_name($var)
    print(list(v_map))



