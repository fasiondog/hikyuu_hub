
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250214"


def part(n: int = 20, band=2.0):
    """
    布林线和常见的看跌 K 线形态（以射击之星为例）作为卖出信号。射击之星的特征是上影线较长，实体较小，且通常出现在上涨趋势中。
    射击之星判断条件:
    ShootingStar:=HIGH - MAX(CLOSE,OPEN) >= 2 * ABS(CLOSE - OPEN) AND MIN(CLOSE,OPEN) - LOW <= ABS(CLOSE - OPEN) / 2;
    卖出信号：触及上轨且出现射击之星
    SellSignal: CLOSE >= UPPER AND ShootingStar;
    """
    local_hub = get_current_hub(__file__)
    boll = get_part(f"{local_hub}.ind.布林线", n=n, band=band)
    upper = RESULT(boll, 1)
    射击之星 = get_part(f"{local_hub}.ind.射击之星")
    sg = SG_OneSide((CLOSE() >= upper) & 射击之星, False)
    sg.name = "卖出触及布林线中轨并反转"
    return sg


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
        "stock_list": ["sz000001"],
        "ktype_list": ["day"],
        "load_history_finance": False,
        "load_weight": False,
        "start_spot": False,
        "spot_worker_num": 1,
    }
    load_hikyuu(**options)

    # 请在下方编写测试代码
    sg = part()
    print(sg)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(Datetime(20231201), Datetime(20240901)))
    sg.to = k

    from matplotlib import pyplot as plt
    k.plot()
    sg.plot(new=False)
    plt.show()
