
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240501"


def part():
    """动态市盈率"""
    EPS = FINANCE(0)
    EPS.set_param("dynamic", True)
    PE = CLOSE / EPS
    PE.name = "动态态市盈率"
    return PE


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    import os
    import sys
    if sys.platform == 'win32':
        os.system('chcp 65001')

    # 仅加载测试需要的数据，请根据需要修改
    options = {
        "stock_list": ["sz000001"],
        "ktype_list": ["day"],
        "load_history_finance": False,
        "load_weight": False,
        "start_spot": False,
        "spot_worker_num": 1,
    }
    load_hikyuu(**options)

    # 请在下方编写测试代码
    ind = part()
    print(ind)

    stk = sm[options['stock_list'][0]]

    import matplotlib.pylab as plt
    k = stk.get_kdata(Query(-200))
    ind(k).plot(label=f"{stk.name}{ind.name}", legend_on=True)
    plt.show()
