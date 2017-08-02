import pickle

# if the ''' has blank , then they will saved
content = '''\
this is my first file_io python
    my name is dean
    i'm a phper
'''
fp = open('test.txt', 'w')
fp.write(content)
fp.close()

fp = open('test.txt')

while True:
    line = fp.readline()
    if len(line) == 0:
        break

    print line,

fp.close()

shopList = [1, 2, 3, 4, 5]
shopTuple = 12, 22, 23, 24, 25

fp = open('test.txt', 'wb')  # write content into file
pickle.dump(shopList, fp)
pickle.dump(shopTuple, fp)

fp.close()

fp = open('test.txt', 'rb')  # read content from file
print pickle.load(fp)
fp.close()

