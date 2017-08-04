def generator_func():
    for i in range(10):
        yield i

for item in generator_func():
    print(item)

generator_str = 'Woooops'
my_iter = iter(generator_str)
print(next(my_iter))  # 已经到下一个元素了
for item in my_iter:  # 内部指针已经到1
    print(item, end='')
    

