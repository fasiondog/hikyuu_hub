
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    os.system('chcp 65001')

from hikyuu import *
try:
    from .part import *
except:
    from part import *

if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        ind = part()
        print(ind)
        exit(0)

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
    ind = part()
    print(ind)
