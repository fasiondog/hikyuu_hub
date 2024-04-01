
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20240202"


def part(n=10, fast_n=2, slow_n=30):
    """收盘价n日AMA均线之上"""
    return CN_Bool(CLOSE() > AMA(CLOSE(), n, fast_n, slow_n))
