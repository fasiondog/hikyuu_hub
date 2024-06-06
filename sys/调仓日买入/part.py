
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240509"


def part():
    """
    仅配合 PF 使用，仅在调仓日发出买入信号使用分配的全部资金买入，默认收盘价买入
    """
    my_sg = SG_Cycle()
    my_mm = MM_Nothing()
    my_sys = SYS_Simple(tm=crtTM(Datetime(20200101)), sg=my_sg, mm=my_mm)
    my_sys.set_param("buy_delay", False)
    return my_sys
