
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240502"


def part(tm: TradeManager, ref_stk=None, adjust_cycle: int = 10, adjust_mode: str = "query",
         delay_to_trading_day: bool = True):
    """
    始终持有沪深300银行指数成分股中市净率最低的股份制银行，每5个交易日检查一次，
    如果发现有新的股份制银行市净率低于原有的股票，则予以换仓。

    :param TradeManager tm: 账户管理实例
    :param Stock ref_stk: 盈利收益参考，默认沪深300
    :param int adjust_cycle: 调仓周期，默认10个交易日
    :param str adjust_mode: 调仓方式
    :param bool delay_to_trading_day: 非交易日调仓时是否延迟到交易日    
    """
    local_hub = get_current_hub(__file__)
    市净率 = get_part("default.ind.市净率")
    stks = [s for s in sm.get_block("指数板块", "300银行")]
    my_pf = get_part(f"{local_hub}.pf.base_最低单因子轮动", tm=tm,
                     ind=市净率, bottomn=2, stks=stks, ref_stk=ref_stk,
                     adjust_cycle=adjust_cycle, adjust_mode=adjust_mode,
                     delay_to_trading_day=delay_to_trading_day)
    return my_pf
