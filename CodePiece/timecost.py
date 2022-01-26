import time
from functools import wraps

LOG_TIME = True

def get_running_time(func):
    # 使用wraps, 保证被装饰过的函数__name__的属性不变
    @wraps(func)
    def inner(*args, **kwargs):
        if LOG_TIME:
            start_time = time.time()
        res = func(*args, **kwargs)
        if LOG_TIME:
            end_time = time.time()
            print('The {} cost time : {}'.format(func.__name__, (end_time - start_time)))
        return res
    return inner


@get_running_time
def test():
    print("test.")

test()
