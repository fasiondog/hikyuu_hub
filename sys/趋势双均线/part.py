
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20240504"

_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(fast_n: int = 10, slow_n: int = 120, tm: TradeManager = _default_tm, mm: MoneyManagerBase = _default_mm, sp: SlippageBase = None):
    """doc"""
    ind = MA(CLOSE, fast_n) > MA(CLOSE, slow_n)
    my_sg = SG_Bool(ind, NOT(ind))
    ret = SYS_Simple(tm=tm, sg=my_sg, mm=mm, sp=sp)
    ret.name = "趋势双均线系统"
    return ret
