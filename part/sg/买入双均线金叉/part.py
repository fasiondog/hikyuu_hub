
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250221"


def part(fastn=5, slown=20):
    """
    短期移动平均线从下向上穿过长期移动平均线，这通常被视为买入信号，意味着短期的市场趋势开始强于长期趋势，股价可能会上涨

    :param fastn: 短期移动平均线周期
    :param slown: 长期移动平均线周期
    :return: part instance
    """
    ret = SG_OneSide(CROSS(MA(CLOSE, fastn), MA(CLOSE, slown)), True)
    ret.name = "买入双均线金叉"
    return ret
