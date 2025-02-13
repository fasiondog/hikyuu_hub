
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250214"


def part(n: int = 20):
    """
    布林线回踩中轨买入

    :param int n: 窗口周期
    """
    local_hub = get_current_hub(__file__)
    sg = SG_OneSide(get_part(f"{local_hub}.ind.布林线回踩中轨", n=n), True)
    sg.name = "买入布林线回踩中轨"
    return sg
