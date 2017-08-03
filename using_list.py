shopList = ['apple', 'mango', 'carrot', 'banana']
# same as php's array 1 Dimensions


print 'I have', len(shopList), '\'s fruits'

print 'There are :'

for item in shopList:
    print item + ' '



print 'total is ', shopList


shopList.append('rice')

shopList.append('miantiao')

print 'now is ', shopList

shopList.pop()

shopList.pop(2) # pops amt

print 'poped is', shopList

del shopList[1]

print 'del is ', shopList

print 'property is ', shopList[1]