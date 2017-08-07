def new_decorator(func):   # 定义装饰器

    def wrapTheFunction():
        print('I am doing some boring work before executing a_function()')

        func()

        print('doing function later')

    return wrapTheFunction


def func_requiring_decoration():
    print('iam the function which needs some decoration to remove')


func_requiring_decoration()

func_requiring_decoration = new_decorator(func_requiring_decoration)

func_requiring_decoration()


@new_decorator   # 使用@运行装饰器
def b_function_requiring_decoration():
    print('i am the function which needs be decoration')


b_function_requiring_decoration()
# OUTPUT:
# I am doing some boring work before executing a_function()
# i am the function which needs be decoration
# doing function later

print(b_function_requiring_decoration.__name__)

