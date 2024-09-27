
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    os.system('chcp 65001')

stk_codes = ['SZ002142', 'SZ000001', 'SH600000', 'SH600015', 'SH600926', 'SH600016', 'SH600919',
             'SH600036', 'SH601009', 'SH601166', 'SH601169', 'SH601229', 'SH601288', 'SH601838',
             'SH601328', 'SH601398', 'SH601658', 'SH601818', 'SH601916', 'SH601939', 'SH601988',
             'SH601998']
os.environ['HKU_STOCK_LIST'] = ";".join(stk_codes)
os.environ['HKU_KTYPE_LIST'] = 'day'  # 加载K线类型（同时包含加载顺序）
# os.environ['HKU_LOAD_STOCK_WEIGHT'] = '1'  # 禁止加载权息数据
os.environ['HKU_LOAD_HISTORY_FINANCE'] = '0'  # 禁止加载历史财务信息
os.environ['HKU_START_SPOT'] = '0'  # 禁止启动行情接收代理

from hikyuu.interactive import *  # NOQA: E402
try:
    from .part import *
except:
    from part import *


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    # if len(sys.argv) > 1:
    #     print("ignore test")
    #     exit(0)

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    # 请在下方编写测试代码
    my_tm = crtTM(Datetime(20200101), init_cash=100000)
    pf = get_part(f"{local_hub}.pf.银行股低市净率轮动", tm=my_tm)
    print(pf)

    if len(sys.argv) <= 1:
        pf.set_param("trace", True)
        query = Query(Datetime(20200101))
        pf.run(query, adjust_cycle=20)

        pf.tm.tocsv(".")

        pf.performance()
        import matplotlib.pylab as plt
        plt.show()
