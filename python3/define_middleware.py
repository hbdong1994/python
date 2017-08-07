from functools import wraps


def passit(threshold=10):   # 定义传递参数的装饰器
    def pass_middleware(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            for i in args:
                if i > threshold:
                    return not_pass()
            return func(*args, **kwargs)
        return decorator
    return pass_middleware


def not_pass():
    print('this is not author to pass')


@passit()
def test_pass(*args, **kwargs):
    print('the items is passed:')
    for i in args:
        print(i)


@passit(15)
def thresh_pass(*args):
    print('the thresh passed is:')
    for i in args:
        print(i)

test_pass(1, 2, 3, 4, 5, 6, 10)
# the items is passed:
# 1
# 2
# 3
# 4
# 5
# 6
# 10
test_pass(9, 10, 11)
# this is not author to pass

thresh_pass(9, 10, 11)
# 9
# 10
# 11
thresh_pass(13, 15 ,16)
# this is not author to pass
