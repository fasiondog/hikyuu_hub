
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu.interactive import *
try:
    from .part import *
except:
    from part import *


if __name__ == "__main__":
    from hikyuu.interactive import *
    import matplotlib.pylab as plt

    import sys
    if sys.platform == 'win32':
        import os
        os.system('chcp 65001')

    # 定义回测日期
    start_date = Datetime(20200101)
    end_date = None
    query = Query(start_date, end_date)

    # 获取指数板块沪深300银行成分股
    stks = [s for s in sm.get_block("指数板块", "300银行")]

    # 选择用于判断的指标，我们直接从 default hub 中获取，如果没更新过，记得 update_hub("default")
    市净率 = get_part("default.ind.市净率")

    # 定义一个多因子评分板
    # 这里 MF 在只有一个因子的情况下，将直接使用因子值本身进行排序
    # 目前 Hikyuu 没有未来函数判断，在单因子的情况下，建议养成习惯右移一位，防止出现未来函数
    # , ref_stk=sm['sh880471'])
    my_mf = MF_EqualWeight([REF(市净率, 1)], stks, query)

    # 先建立一个股票到实际运行的系统策略的映射
    def calculate(self):
        self.stk_sys_dict = dict([(s.get_stock(), s)
                                 for s in self.real_sys_list])

    # 实现选股策略中每日选取的系统
    @hku_catch(ret=ScoreRecordList(), trace=True)
    def get_selected(self, date):
        scores = self.mf.get_scores(date)
        if len(scores) < 2:
            return []
        return [SystemWeight(self.stk_sys_dict[scores[-1].stock], scores[-1].value),
                SystemWeight(self.stk_sys_dict[scores[-2].stock], scores[-2].value)]

    my_se = crtSE(calculate, get_selected=get_selected)
    my_se.mf = my_mf

    my_sg = SG_Cycle()
    # my_sg = SG_AllwaysBuy()
    my_mm = MM_Nothing()
    my_sys = SYS_Simple(tm=crtTM(start_date), sg=my_sg, mm=my_mm)
    my_sys.set_param("buy_delay", False)
    my_sys.set_param("trace", True)

    my_se = my_se.clone()
    my_se.add_stock_list(stks, my_sys)

    my_af = AF_EqualWeight()
    my_tm = crtTM(start_date, init_cash=100000)  # , cost_func=TC_FixedA2017())
    pf = PF_Simple(tm=my_tm, af=my_af, se=my_se)
    pf.set_param("trace", True)
    pf.run(query, adjust_cycle=20)
    pf.performance()  # ref_stk=sm['sh880471'])

    my_tm.tocsv(".")
    print(my_tm)
    plt.show()
