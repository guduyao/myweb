# -*- coding: UTF-8 -*-     
# @IDE      ：PyCharm
# @Author   ：guduyao
# @Date     ：2021/8/5 17:38

import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper