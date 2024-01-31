
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

try:
    from .mypart import *
except:
    from mypart import *

author = "fasiondog"
version = "20240201"


def part(n=100):
    """n日均线之上"""
    return my_part(n)


if __name__ == "__main__":
    ind = part()
    print(ind)
