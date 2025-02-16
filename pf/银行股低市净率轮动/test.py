
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    os.system('chcp 65001')


if __name__ == "__main__":
    from hikyuu import *

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
