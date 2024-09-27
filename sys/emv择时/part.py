
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240526"


def part(n: int = 14, tm: TradeManager = None) -> System:
    """
    使用简易波动率指标（EMV）的交易系统。
    EMV 在0 以下表示弱势，在0 以上表示强势；EMV 由负转正应买进，由正转负应卖出。
    """
    local_hub = get_current_hub(__file__)
    emv = get_part(f'{local_hub}.ind.emv', n=n)
    my_sg = SG_Bool(emv > 0, emv <= 0)
    my_tm = crtTM() if tm is None else tm
    my_mm = MM_Nothing()
    my_mm.set_param("auto-checkin", False)
    my_sys = SYS_Simple(tm=my_tm, sg=my_sg, mm=my_mm)
    return my_sys
