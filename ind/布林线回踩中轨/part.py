
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250213"


def part(n=20):
    """
    布林线回踩中轨买入：价格在上涨过程中，有时会回调至布林线中轨附近，若中轨能对价格起到支撑作用，
    价格在此处止跌企稳并再次向上，是较好的买入时机，表明中轨的支撑有效，上涨趋势有望延续。
    其本质就是均线回踩，通常需要配合长期趋势，比如价格在长期200日均线智商

    :param n: 均线周期
    :return: 布林线回踩中轨指标
    """
    ma = MA(CLOSE(), n=n)
    #  前一日收盘价大于中轨，当日最低价小于等于中轨且收盘价大于中轨
    ret = (REF(CLOSE(), 1) > ma) & (LOW() <= ma) & (CLOSE() > ma)
    ret.name = '布林线回踩中轨'
    return ret
