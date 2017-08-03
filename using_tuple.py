# shopList = [1,2,3]
#
# tuple_dev = [1,2, shopList]
#
# print 'the tuple is ', tuple_dev
#
# tuple_dev.append(3)
#
# print 'now tuple is ', tuple_dev
#
shopList = 1,2,3 # define tuple param

tuple_dev = 1,2,shopList

print 'the tuple is ', tuple_dev, 'len is ', len(tuple_dev)

for item in tuple_dev:
    if not isinstance(item, tuple):  # detect double param is same obj
        print item
    else:
        print 'children tuple:',
        for k in item:
            print k,

print
print 'index 1 is', tuple_dev[1]

print 'children tuple is ', tuple_dev[2][1]
