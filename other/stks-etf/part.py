
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240601"


def part():
    """获取所有ETF"""
    return [s for s in sm if s.type == constant.STOCKTYPE_ETF]


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    from hikyuu.interactive import *

    # 请在下方编写测试代码
    ind = part()
    print(ind)
