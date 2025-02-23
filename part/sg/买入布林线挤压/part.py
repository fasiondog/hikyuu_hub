
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(boll_n: int = 20, band: float = 2.0, squeeze_n: int = 50):
    """
    布林线宽度在 squeeze_n 周期内为最小值时买入

    :param boll_n: 布林线周期
    :param band: 布林线带宽
    :param squeeze_n: 布林线宽度在 squeeze_n 周期内为最小值时买入
    """
    sd = DISCARD(STDEV(CLOSE(), n=boll_n), discard=boll_n)
    squeeze = LLV(sd, n=squeeze_n)
    ret = SG_OneSide(sd == squeeze, True)
    ret.name = "买入布林线挤压"
    return ret
