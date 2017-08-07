from functools import wraps


def new_decorator(func):
    @wraps(func)
    def wrapTheFunction(*args):     # 通过functools防止 装饰器函数重写函数 doc
        print("I am doing some boring work before executing a_func()")
        print('global', name)   # 可以调用外部变量
        func(*args)
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction


@new_decorator
def function_requiring_decoration(*args):
    print('im decoration function', args)

name = 'dean'

function_requiring_decoration(1, 3)

print(function_requiring_decoration.__name__)   # 如果不用functools 则会输出 装饰器函数名 即 wrapTheFunction
