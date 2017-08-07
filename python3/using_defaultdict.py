import collections
import json

# some_dict = {}
# some_dict['colors']['favourite'] = 'yellow'
#
# print(some_dict)

tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
print(some_dict)
print(json.dumps(some_dict))   # 用json.dumps 输出json串

some_dict['colours']['lover'] = 'apple'

colours = (
    ('Yasoob', ('Yellow', 'red')),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = collections.Counter(name for name, colour in colours)
print(favs)


