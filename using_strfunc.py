import os
name = 'Swaroop'

if name.startswith('Swa'):
    print 'Yes, the string is start with Swa'
if name.endswith('oop'):
    print 'Yes, the string is end with oop'
if name.find('dean') == -1:
    print 'Woops, the string not contain dean'

delimiter = ','

mylist = ['Brazil', 'Russia', 'India', 'China']

print delimiter.join(mylist) # convert list to string

union = ','
mystr = 'Brazil, Russia, India, China'+ \
    'das, sadsa, 224' + \
    'date, aaa, 421'
print mystr.split(union) # convert string to list

print os.sep