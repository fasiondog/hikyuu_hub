
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20250213"


def part(n=20, band=2.0):
    """
    布林线由三条线组成，即上轨线、中轨线和下轨线。
    中轨线通常是价格的移动平均线，上轨线和下轨线则分别位于中轨线的上方和下方一定标准差的位置

    该指标指标集为4个, 0: 中轨线, 1: 上轨线, 2: 下轨线, 3: 轨道宽度

    : param int n: 移动平均线周期, 默认20
    : param float band: 轨道宽度（中轨距离 band 倍标准差处
    : return: 布林线
    : rtype: hikyuu.indicator.Indicator
    """
    ma = DISCARD(MA(CLOSE(), n=n), discard=n)
    sd = DISCARD(STDEV(CLOSE(), n=n), discard=n)
    top = ma + band * sd
    bottom = ma - band * sd
    width = 2 * band * sd
    ret = WEAVE(ma, WEAVE(top, WEAVE(bottom, width)))
    ret.name = '布林线'
    return ret


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        ind = part()
        print(ind)
        exit(0)

    import os
    import sys
    if sys.platform == 'win32':
        os.system('chcp 65001')

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
    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-100))

    ind = part()
    x = ind(k)
    print(x)

    import matplotlib.pyplot as plt
    mb = RESULT(x, 0)
    mb.name = "Middle Band"
    ub = RESULT(x, 1)
    ub.name = "Upper Band"
    lb = RESULT(x, 2)
    lb.name = "Lower Band"

    mb.plot(legend_on=True)
    ub.plot(new=False, legend_on=True)
    lb.plot(new=False, legend_on=True)

    width = RESULT(x, 3)
    width.plot(legend_on=True)
    plt.show()
