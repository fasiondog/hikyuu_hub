
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

try:
    from .mypart import *
except:
    from mypart import *

author = "fasiondog"
version = "20240202"


def part(n=10, fast_n=2, slow_n=30):
    """收盘价n日AMA均线之上"""
    return my_part(n, fast_n, slow_n)


if __name__ == "__main__":
    ind = part()
    print(ind)
