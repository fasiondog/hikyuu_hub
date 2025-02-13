
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250214"


def part(n: int = 3, boll_n: int = 20):
    """
    连续 N 日收盘价低于布林线中轨

    :param n: 连续 N 日收盘价低于布林线中轨, 默认3
    :param boll_n: 布林线周期, 默认20
    :return: 卖出收盘价连续3日跌破布林线中轨信号
    """
    sg = SG_OneSide(COUNT(CLOSE() < MA(CLOSE(), n=boll_n), n=n), False)
    sg.name = "卖出收盘价连续N日跌破布林线中轨"
    return sg
