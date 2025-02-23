
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(n: int = 20, band=2.0):
    """
    收盘价跌破布林新下轨时卖出

    :param n: 布林线周期, 默认20
    :param float band: 布林线带宽, 默认2.0
    :return: 卖出收盘价跌破布林线新下轨信号
    """
    local_hub = get_current_hub(__file__)
    ind = RESULT(get_part(f"{local_hub}.ind.布林线", n=n, band=band), 2)
    sg = SG_OneSide(CLOSE() < ind, False)
    sg.name = "卖出收盘价跌破布林线下轨"
    return sg
