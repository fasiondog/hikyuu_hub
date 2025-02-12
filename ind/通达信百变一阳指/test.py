
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    os.system('chcp 65001')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    from hikyuu import *
    try:
        from .part import *
    except:
        from part import *

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

    ind(k).plot()
    import matplotlib.pyplot as plt
    plt.show()
