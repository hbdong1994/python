def testFuncName(param1, *args, **kwargs):  # *args means yuanzu **kwargs means directory
    total = 0
    for i in args:
        print i
    # print args
    print args
    print kwargs

testFuncName(0, [1, 2, 3, 4], name='dean', age=17, phone='18883273127')
