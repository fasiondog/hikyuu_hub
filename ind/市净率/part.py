
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240502"


def part():
    """市净率=每股市价／每股净资产"""
    ret = CLOSE/FINANCE(3)
    ret.name = "市净率"
    return ret
