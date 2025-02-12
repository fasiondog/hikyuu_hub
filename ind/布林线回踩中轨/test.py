
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    os.system('chcp 65001')

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

    # 仅加载测试需要的数据，请根据需要修改
    options = {
        "stock_list": ["sh000001"],
        "ktype_list": ["day"],
        "load_history_finance": False,
        "load_weight": False,
        "start_spot": False,
        "spot_worker_num": 1,
    }
    load_hikyuu(**options)

    # 请在下方编写测试代码
    s = sm['sh000001']
    k = s.get_kdata(Query(-200))
    ind = part()
    x = ind(k)
    print(x)

    # local_hub = get_current_hub(__file__)
    # update_hub(local_hub)

    # bull = get_part(f"{local_hub}.ind.布林线")(k)
    # import matplotlib.pyplot as plt
    # ax1, ax2 = create_figure(2)
    # k.plot(axes=ax1)
    # DRAWICON(x, RESULT(bull, 2), 1, kdata=k, axes=ax1)
    # RESULT(bull, 0).plot(axes=ax1)
    # RESULT(bull, 1).plot(axes=ax1)
    # RESULT(bull, 2).plot(axes=ax1)
    # x.plot(axes=ax2, legend_on=True)
    # plt.show()
