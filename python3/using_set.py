# to generate set    in the set . could not have duplicate value
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# x for x in list if item is true  list数据结构 使用 循环list 如果if条件满足 则返回此循环x
duplicates = set([x for x in some_list if some_list.count(x) > 1])


valid = set(['yellow', 'red', 'blue', 'green', 'black'])   # replace { to set[( generate a set
input_set = {'red', 'brown'}
print(input_set.intersection(valid))  # 查询交集
# 输出: set(['red'])

print(input_set.difference(valid))   # 查询差集
# 输出： {'brown'}

print(input_set.union(valid))   # 获取并集

fat = False
print('im fat' if fat else 'im not fat')   #三元运算符
