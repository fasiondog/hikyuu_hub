
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    os.system('chcp 65001')

os.environ['HKU_STOCK_LIST'] = "sz000001"  # 加载指定的证券
os.environ['HKU_KTYPE_LIST'] = 'day'  # 加载K线类型（同时包含加载顺序）
os.environ['HKU_LOAD_STOCK_WEIGHT'] = '0'  # 禁止加载权息数据
os.environ['HKU_LOAD_HISTORY_FINANCE'] = '0'  # 禁止加载历史财务信息
os.environ['HKU_START_SPOT'] = '0'  # 禁止启动行情接收代理

from hikyuu.interactive import *  # NOQA: E402
try:
    from .part import *
except:
    from part import *


if __name__ == "__main__":
    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    my_sys = get_part(f"{local_hub}.sys.emv择时")
    print(my_sys)

    if len(sys.argv) <= 1:
        import matplotlib.pylab as plt
        stk = sm['sz000001']
        # my_tm = crtTM(Datetime(20120101), init_cash=100000,
        #               cost_func=TC_FixedA2017())
        # my_sys.tm = my_tm
        my_sys.run(stk, Query(Datetime(20120101)))
        my_sys.performance()
        plt.show()
