
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu.interactive import *
try:
    from .part import *
except:
    from part import *

if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    # if len(sys.argv) > 1:
    #     print("ignore test")
    #     exit(0)

    # 请在下方编写测试代码
    my_se = part()
    stks = [s for s in sm.get_block("指数板块", "300银行")]
    my_se.prepare(Query(Datetime(20200101)), stks)

    print(my_se)
    print(my_se.mf)
