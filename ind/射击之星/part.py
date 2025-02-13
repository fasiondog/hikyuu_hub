
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250213"


def part():
    """
    射击之星的特征是上影线较长，通达信公式：
    ShootingStar:=HIGH - MAX(CLOSE,OPEN) >= 2 * ABS(CLOSE - OPEN) AND MIN(CLOSE,OPEN) - LOW <= ABS(CLOSE - OPEN) / 2;
    """
    ret = (HIGH() - MAX(CLOSE(), OPEN()) >= 2 * ABS(CLOSE() - OPEN())
           ) & ((MIN(CLOSE(), OPEN()) - LOW()) <= ABS(CLOSE() - OPEN()) / 2)
    ret.name = "射击之星"
    return ret
