from functools import wraps


class Logit:
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrap_function(*args, **kwargs):
            log_str = func.__name__ + ' was called'
            print(log_str)
            with open(self.logfile, 'a') as open_file:   # 用 with open as 来处理文件句柄操作
                open_file.write(log_str+'\n')
            self.notify(log_str)
            return func(*args, **kwargs)
        return wrap_function

    @staticmethod
    def notify(str):
        print('str[', str, '] has been logged')


@Logit()
def myfunc():
    print('this is my func')

myfunc()
