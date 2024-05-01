
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
    ind = part()
    print(ind)

    import matplotlib.pylab as plt
    k = get_kdata("sz000001", Query(-200))
    ind(k).plot(label="平安银行静态市盈率", legend_on=True)
    plt.show()
