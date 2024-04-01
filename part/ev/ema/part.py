
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20240222"


def part(n=100, market="SH"):
    """doc"""
    return EV_Bool(CLOSE() > EMA(CLOSE(), n), market)
