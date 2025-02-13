
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250214"


def part(boll_n: int = 20, band: float = 2.0, ma_n: int = 100):
    """
    系统条件: 收盘价大于 ma_n 日均线进行
    买入: 布林线回踩中轨
    卖出: 卖出触及布林线中轨并反转

    :param boll_n: 布林线周期
    :param band: 布林线带宽
    :param ma_n: 系统条件中均线周期
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入布林线回踩中轨", n=boll_n)
    sg2 = get_part(f"{local_hub}.sg.卖出触及布林线中轨并反转", n=boll_n, band=band)
    sg = sg1 + sg2
    sg.set_param("alternate", True)
    # my_sys = SYS_Simple(sg=sg)
    my_sys = SYS_Simple(sg=sg, cn=get_part(f"{local_hub}.cn.ma", n=ma_n))
    my_sys.name = "布林线回踩策略1"
    return my_sys
