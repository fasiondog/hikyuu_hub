
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

try:
    from .mypart import *
except:
    from mypart import *

author = "fasiondog"
version = "20240222"


def part(n=100, market="SH"):
    """doc"""
    return my_part(n, market)


if __name__ == "__main__":
    ind = part()
    print(ind)
