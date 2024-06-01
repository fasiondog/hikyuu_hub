
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

    n = 100
    band = 0.5
    my_sg = get_part(f"{local_hub}.sg.趋势布林带", n=n, band=band)
    print(my_sg)

    if len(sys.argv) <= 1:
        stk = sm['sz000001']
        k = stk.get_kdata(Query(-2000))
        ma = MA(CLOSE, n)
        top = ma + band * STDEV(CLOSE, n)
        top.name = "上轨"
        bottom = ma - band * STDEV(CLOSE, n)
        bottom.name = "下轨"

        k.close.plot(legend_on=True)
        ma(k).plot(new=False, legend_on=True)
        top(k).plot(new=False, legend_on=True)
        bottom(k).plot(new=False, legend_on=True)

        my_sg.to = k
        my_sg.plot(new=False)
        gca().set_title(stk.name)

        import matplotlib.pylab as plt
        plt.show()
