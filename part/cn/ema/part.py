
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

try:
    from .mypart import *
except:
    from mypart import *

author = "fasiondog"
version = "20240202"


def part(n=100):
    """收盘价n日EMA均线之上"""
    return my_part(n)


if __name__ == "__main__":
    ind = part()
    print(ind)
