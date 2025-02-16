
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Sequence
from hikyuu import *

author = "admin"
version = "20240514"


def part(tm: TradeManager, ind: Indicator, bottomn: int = 2, stks: Sequence = None,
         ref_stk: Stock = None, adjust_cycle: int = 10, adjust_mode: str = "query",
         delay_to_trading_day: bool = True):
    """
    始终持有沪深300银行指数成分股中市净率最低的股份制银行，每5个交易日检查一次，
    如果发现有新的股份制银行市净率低于原有的股票，则予以换仓。

    :param TradeManager tm: 账户管理实例
    :param Indicator ind: 单因子值
    :param int bottomn: 最低的 bottomn 支证券
    :param Sequence stks: 轮动的证券序列
    :param Stock ref_stk: 回测参考证券，默认沪深300
    :param int adjust_cycle: 调仓周期，默认10个交易日
    :param str adjust_mode: 调仓方式
    :param bool delay_to_trading_day: 非交易日调仓时是否延迟到交易日
    """
    local_hub = get_current_hub(__file__)
    my_se = get_part(f"{local_hub}.se.最低单因子", ind=ind, bottomn=bottomn)
    if ref_stk is None:
        my_se.set_param("ref_stk", get_stock("sh000300"))
    my_sys = get_part(f"{local_hub}.sys.调仓日买入")
    my_se.add_stock_list(stks, my_sys)

    my_af = AF_EqualWeight()
    my_pf = PF_Simple(tm=tm, af=my_af, se=my_se, adjust_cycle=adjust_cycle,
                      adjust_mode=adjust_mode, delay_to_trading_day=delay_to_trading_day)
    return my_pf
