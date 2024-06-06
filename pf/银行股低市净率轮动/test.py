
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
        pf = pf.prepare(pf, query)
        pf.run(query, adjust_cycle=20)
        pf.performance()

        import matplotlib.pylab as plt
        plt.show()
