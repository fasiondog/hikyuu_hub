
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(boll_n: int = 20, band: float = 2.0, squeeze_n: int = 50):
    """
    布林线挤压策略
    进入信号: 当股价突破上轨或出现Squeeze。
    退出信号: 当股价跌破下轨。

    :param boll_n: 布林线周期, 默认20
    :param band: 布林线带宽, 默认2.0
    :param squeeze_n: 移动平均周期, 50
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入收盘价突破布林线上轨", n=boll_n, band=band)
    sg2 = get_part(f"{local_hub}.sg.买入布林线挤压", boll_n=boll_n,
                   band=band, squeeze_n=squeeze_n)
    sg3 = get_part(f"{local_hub}.sg.卖出收盘价跌破布林线下轨", n=boll_n, band=band)
    sg = SG_Add(sg1, sg2, False) + sg3
    my_sys = SYS_Simple(sg=sg)
    my_sys.name = "布林线挤压策略"
    return my_sys
