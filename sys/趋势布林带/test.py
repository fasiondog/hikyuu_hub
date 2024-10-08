
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    os.system('chcp 65001')

os.environ['HKU_STOCK_LIST'] = "sz000001"  # 仅加载指定的证券
os.environ['HKU_KTYPE_LIST'] = 'day'  # 加载K线类型（同时包含加载顺序）
# os.environ['HKU_LOAD_STOCK_WEIGHT'] = '0'  # 禁止加载权息数据
# os.environ['HKU_LOAD_HISTORY_FINANCE'] = '0'  # 禁止加载历史财务信息
# os.environ['HKU_START_SPOT'] = '0'  # 禁止启动行情接收代理

from hikyuu.interactive import *  # NOQA: E402
try:
    from .part import *
except:
    from part import *

if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    # if len(sys.argv) <= 1:
    #     print("ignore test")
    #     exit(0)

    # 请在下方编写测试代码
    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    my_sys = get_part(f"{local_hub}.sys.趋势布林带")
    print(my_sys)

    if len(sys.argv) <= 1:
        my_tm = crtTM(Datetime(20200101), init_cash=100000,
                      cost_func=TC_FixedA2017())
        my_sys.tm = my_tm
        my_sys.run(sm['sz000001'], Query(Datetime(20200101)))
        print(my_sys.tm)
        my_sys.tm.tocsv(os.path.dirname(os.path.abspath(__file__)))
        my_sys.performance()
        import matplotlib.pylab as plt
        plt.show()
