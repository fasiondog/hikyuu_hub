
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu.interactive import *
try:
    from .part import *
except:
    from part import *

import sys
if sys.platform == 'win32':
    import os
    os.system('chcp 65001')

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
