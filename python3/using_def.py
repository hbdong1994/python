def hi(name='Yasoob'):
    print('hi', name)

    def greet(age=17):
        return 'bellow hi function greet, age:' + age.__str__()

    def welcome(country='china'):
        return 'bellow hi function welcome, country:'+country
    # return 'hi'+name
    if name == 'dean':
       return greet    # 返回变量 不返回函数 因为返回函数名变量 可以被传递 灵活性较高
    else:
       return welcome

a = hi('dean')     # 函数返回函数结果

print(a(16))

b = hi('sean')

print(b('usa'))


# multiname func
# print(hi('dean'))

# multiname = hi

# print(multiname('dean'))

# del hi
#
# print(hi())
#
# print(multiname())
