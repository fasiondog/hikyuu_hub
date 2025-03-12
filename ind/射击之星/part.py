
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250213"


def part():
    """
    射击之星的特征是上影线较长，通达信公式：
    ShootingStar:=HIGH - MAX(CLOSE,OPEN) >= 2 * ABS(CLOSE - OPEN) AND MIN(CLOSE,OPEN) - LOW <= ABS(CLOSE - OPEN) / 2;
    """
    ret = (HIGH() - MAX(CLOSE(), OPEN()) >= 2 * ABS(CLOSE() - OPEN())
           ) & ((MIN(CLOSE(), OPEN()) - LOW()) <= ABS(CLOSE() - OPEN()) / 2)
    ret.name = "射击之星"
    return ret


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

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
    s = sm[options['stock_list'][0]]
    print(s)
    k = s.get_kdata(Query(-300))
    ind = part()
    x = ind(k)
    print(x)

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    bull = get_part(f"{local_hub}.ind.布林线")(k)
    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    DRAWICON(x, RESULT(bull, 2), 11, kdata=k, axes=ax1)
    RESULT(bull, 0).plot(axes=ax1)
    RESULT(bull, 1).plot(axes=ax1)
    RESULT(bull, 2).plot(axes=ax1)
    x.plot(axes=ax2, legend_on=True)
    plt.show()
