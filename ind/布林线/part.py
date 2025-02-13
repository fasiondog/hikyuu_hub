
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20250213"


def part(n=20, band=2.0):
    """
    布林线由三条线组成，即上轨线、中轨线和下轨线。
    中轨线通常是价格的移动平均线，上轨线和下轨线则分别位于中轨线的上方和下方一定标准差的位置

    该指标指标集为3个, 0: 中轨线, 1: 上轨线, 2: 下轨线

    : param int n: 移动平均线周期, 默认20
    : param float band: 轨道宽度（中轨距离 band 倍标准差处
    : return: 布林线
    : rtype: hikyuu.indicator.Indicator
    """
    ma = MA(CLOSE(), n=n)
    sd = STDEV(CLOSE(), n=n)
    top = ma + band * sd
    bottom = ma - band * sd
    ret = WEAVE(ma, WEAVE(top, bottom))
    ret.name = '布林线'
    return ret
