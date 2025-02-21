
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250221"


def part(fastn=5, slown=20):
    """
    短期移动平均线从上向下穿过长期移动平均线，这一般被看作卖出信号，表明短期市场趋势转弱，股价可能会下跌。

    :param fastn: 短期移动平均线周期
    :param slown: 长期移动平均线周期
    :return: part instance
    """
    ret = SG_OneSide(CROSS(MA(CLOSE, slown), MA(CLOSE, fastn)), False)
    ret.name = "卖出双均线死叉"
    return ret
