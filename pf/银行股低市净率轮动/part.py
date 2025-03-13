
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
    市净率 = get_part("default.ind.市净率")
    stks = tuple([s for s in sm.get_block("指数板块", "300银行")])
    my_pf = get_part("default.pf.base_最低单因子轮动", tm=tm,
                     ind=市净率, bottomn=2, stks=stks, ref_stk=ref_stk,
                     adjust_cycle=adjust_cycle, adjust_mode=adjust_mode,
                     delay_to_trading_day=delay_to_trading_day)
    return my_pf


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    import sys
    if sys.platform == 'win32':
        import os
        os.system('chcp 65001')

    options = {
        "stock_list": ['SZ002142', 'SZ000001', 'SH600000', 'SH600015', 'SH600926', 'SH600016', 'SH600919',
                       'SH600036', 'SH601009', 'SH601166', 'SH601169', 'SH601229', 'SH601288', 'SH601838',
                       'SH601328', 'SH601398', 'SH601658', 'SH601818', 'SH601916', 'SH601939', 'SH601988',
                       'SH601998'],
        "ktype_list": ['day'],
        "load_history_finance": False,
        "start_spot": False
    }
    load_hikyuu(**options)

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    # 请在下方编写测试代码
    my_tm = crtTM(Datetime(20200101), init_cash=100000)
    pf = get_part(f"{local_hub}.pf.银行股低市净率轮动", tm=my_tm, adjust_cycle=20)
    print(pf)

    if len(sys.argv) <= 1:
        pf.set_param("trace", True)
        query = Query(Datetime(20200101))
        pf.run(query)

        pf.tm.tocsv(".")

        pf.performance()
        import matplotlib.pylab as plt
        plt.show()
