
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Sequence
from hikyuu import *

author = "admin"
version = "20240514"


# pf 目前无法使用 __class__ 的方法，原因未知
# 目前必须使用对象的方法最替代
def pf_prepare(self, query, stks=None):
    local_hub = get_current_hub(__file__)
    my_sys = get_part(f"{local_hub}.sys.调仓日买入")
    my_se = get_part(f"{local_hub}.se.最低单因子",
                     ind=self.ind, bottomn=self.bottomn)
    my_se.prepare(query, self.stks if stks is None else stks, self.ref_stk)
    my_se.add_stock_list(self.stks, my_sys)
    self.se = my_se
    return self.clone()


def part(tm: TradeManager, ind: Indicator, bottomn: int = 2, stks: Sequence = None, ref_stk: Stock = None):
    """
    始终持有沪深300银行指数成分股中市净率最低的股份制银行，每5个交易日检查一次，
    如果发现有新的股份制银行市净率低于原有的股票，则予以换仓。

    :param TradeManager tm: 账户管理实例
    :param Indicator ind: 单因子值
    :param int bottomn: 最低的 bottomn 支证券
    :param Sequence stks: 轮动的证券序列
    :param Stock ref_stk: 回测参考证券，默认沪深300
    """
    my_af = AF_EqualWeight()
    my_pf = PF_Simple(tm=tm, af=my_af)
    if ref_stk is None:
        my_pf.ref_stk = get_stock("sh000300")
    my_pf.ind = ind
    my_pf.bottomn = bottomn
    my_pf.stks = stks
    my_pf.prepare = pf_prepare
    return my_pf
