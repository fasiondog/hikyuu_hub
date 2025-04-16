from hikyuu import *

# 部件作者
author = "fasiondog"

# 版本
version = '20231223'

TK = (OPEN() > REF(HIGH(), 1)) & (LOW() > REF(HIGH(), 1))
TS = BARSLAST(TK)
XG = BETWEEN(CLOSE(), REF(HIGH(), TS+1), REF(LOW(), TS)) & (TS < 10)


def part():
    """
    通达信向上跳空选股器
    """
    XG.name = "通达信向上跳空"
    return XG


if __name__ == '__main__':
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

    k = get_kdata("sz000001", Query(-300))
    ind = part()
    print(ind)

    k.plot()
    ax2 = gca().twinx()
    ind(k).plot(axes=ax2)
    import matplotlib.pyplot as plt
    plt.show()
