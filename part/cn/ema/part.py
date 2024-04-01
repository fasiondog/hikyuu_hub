
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20240202"


def part(n=100):
    """收盘价n日EMA均线之上"""
    return CN_Bool(CLOSE() > EMA(CLOSE(), n))
