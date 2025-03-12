
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250221"


def part(fastn=5, slown=20):
    """
    短期移动平均线从下向上穿过长期移动平均线，这通常被视为买入信号，意味着短期的市场趋势开始强于长期趋势，股价可能会上涨

    :param fastn: 短期移动平均线周期
    :param slown: 长期移动平均线周期
    :return: part instance
    """
    ret = SG_OneSide(CROSS(MA(CLOSE, fastn), MA(CLOSE, slown)), True)
    ret.name = "买入双均线金叉"
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
    fastn = 5
    slown = 20
    sg = part(fastn=5, slown=20)
    print(sg)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-200))
    sg.to = k

    k.plot()
    sg.plot(new=False)
    MA(CLOSE, fastn)(k).plot(new=False)
    MA(CLOSE, slown)(k).plot(new=False)

    import matplotlib.pyplot as plt
    plt.show()
