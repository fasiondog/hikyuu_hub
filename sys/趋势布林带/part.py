
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240517"


_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(n: int = 100, band: float = 0.5, tm: TradeManager = None) -> System:
    """
    布林带趋势交易策略：当股价向上突破上轨时，为买入信号，当股价向下突破下界时，则为卖出信号

    :param int n: 窗口周期，默认 100
    :param float band: 轨道宽度, 默认 0.5
    :param TradeManager tm: 账户管理实例，未指定时，默认使用 crtTM()
    """
    local_hub = get_current_hub(__file__)
    my_sg = get_part(f"{local_hub}.sg.趋势布林带", n=n, band=band)
    my_tm = crtTM() if tm is None else tm
    my_sys = SYS_Simple(tm=my_tm, mm=MM_Nothing(), sg=my_sg)
    return my_sys.clone()
