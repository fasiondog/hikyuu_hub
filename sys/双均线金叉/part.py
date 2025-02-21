
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250221"


def part(fastn=5, slown=20):
    """
    双均线金叉系统是一种常见且基础的技术分析交易策略，它基于两条不同周期的移动平均线（MA）的交叉情况来产生买卖信号。

    :param fastn: 短期移动平均线周期
    :param slown: 长期移动平均线周期
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入双均线金叉", fastn=fastn, slown=slown)
    sg2 = get_part(f"{local_hub}.sg.卖出双均线死叉", fastn=fastn, slown=slown)
    sg = sg1 + sg2
    my_sys = SYS_Simple(sg=sg)
    my_sys.name = "双均线金叉"
    return my_sys
