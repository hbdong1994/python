import datetime

date = datetime.datetime.today()

# convert to string
print date.__str__()

ab = {
    'Author' : 'dena',
    'First Name': 'hbdong',
    'Last Name': 'father',
    'Date': date.__str__()
}

print 'the dict is ', ab

print 'string format : '

ab['Country'] = 'China'

ab.pop('Country') # pop property

for item, value in ab.items(): # foreach the tulpe
    print 'the {} is {}'.format(item, value)