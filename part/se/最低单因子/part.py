
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240514"


# 先建立一个股票到实际运行的系统策略的映射
def _calculate(self):
    self.stk_sys_dict = dict([(s.get_stock(), s)
                             for s in self.real_sys_list])


# 实现选股策略中每日选取的系统
@hku_catch(ret=[], trace=True)
def _get_selected(self, date):
    ret = []
    scores = self.mf.get_scores(date)
    if not scores:
        return ret

    bottomn = self.get_param("bottomn")
    count = 0
    for i in range(len(scores)-1, -1, -1):
        if not isnan(scores[i].value) and not isinf(scores[i].value):
            ret.append(SystemWeight(
                self.stk_sys_dict[scores[i].stock], scores[i].value))
            count += 1
            if count >= bottomn:
                break
    return ret


def prepare(self, query, stks, ref_stk=None):
    self.mf.query = query
    self.mf.set_stock_list(stks)
    self.mf.set_ref_stock(
        ref_stk if ref_stk is not None else get_stock("sh000300"))


def part(ind: Indicator, bottomn: int = 2):
    """
    选取因子值最低的 bottomn 支证券, 使用前，需要先使用 prepare 设置相关参数

    :param Indicator ind: 单因子
    :param int bottomn: 选取因子值最低的 bottomn 支证券
    """
    my_se = crtSE(_calculate, get_selected=_get_selected,
                  params={'bottomn': 2})
    my_se.mf = MF_EqualWeight()
    my_se.mf.set_ref_indicators([REF(ind, 1)])
    my_se.__class__.prepare = prepare
    return my_se
