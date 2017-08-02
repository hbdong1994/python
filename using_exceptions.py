# encoding=UTF-8


class SelfDefineException(Exception):
    def __init__(self, name, length, atleast):
        Exception.__init__(self)

        self.name = name
        self.len = length
        self.max = atleast


try:
    something = input('Input:')  # console input must contained by ''
    print something
    if len(something) <= 3:
        raise SelfDefineException('dean', len(something), 3)

    print 123141

except SelfDefineException as ex:
    print ex.name, ex.len, ex.max
else:
    print something
