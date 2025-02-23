
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(n: int = 20, band: float = 2.0):
    """
    收盘价突破布林线上轨时买入

    :param int n: 布林线周期, 默认20
    :param float band: 布林线带宽, 默认2.0
    :return: 买入收盘价突破布林线上轨信号
    """
    local_hub = get_current_hub(__file__)
    ind = RESULT(get_part(f"{local_hub}.ind.布林线", n=n, band=band), 1)
    sg = SG_OneSide(CLOSE() > ind, True)
    sg.name = "卖出收盘价跌破布林新下轨"
    return sg
