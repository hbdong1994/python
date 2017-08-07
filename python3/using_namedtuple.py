from collections import namedtuple
import json

common_tuple = 1, 2, 3, 4

print(common_tuple)
print(common_tuple[0])

# common_tuple[0] = 1  # error
list = [1, 2, 3, 4]
list[0] = 2  # list can be modify
print(list)

people = namedtuple('people', 'name age country')

dean = people(name='dean', age='18', country='china')
print(dean)

# dean.name = 'sean'   # nametuple is same sa tuple, not be modified

print(dean._asdict())  # nametuple can turn to be dict
# out : OrderedDict([('name', 'dean'), ('age', '18'), ('country', 'china')])

print(json.dumps(dean))
# out : ["dean", "18", "china"]
print(json.dumps(dean._asdict()))
# out : {"name": "dean", "age": "18", "country": "china"}
