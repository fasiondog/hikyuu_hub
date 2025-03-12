
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240517"


class SG_BuLin(SignalBase):
    def __init__(self, n=100, band=0.5):
        super(SG_BuLin, self).__init__("SG_BuLin")
        self.set_param("n", int(n))
        self.set_param("band", float(band))

    def _calculate(self, k):
        n = self.get_param("n")
        band = self.get_param("band")
        c = k.close
        ma = MA(c, n)
        sd = STDEV(c, n)
        top = ma + band * sd
        bottom = ma - band * sd
        for i in range(len(c)):
            if c[i] > top[i]:
                self._add_buy_signal(k[i].datetime)
            elif c[i] < bottom[i]:
                self._add_sell_signal(k[i].datetime)

    def _clone(self):
        cloned = SG_BuLin(self.get_param("n"), self.get_param("band"))
        return cloned


def bulindai_calculate(self: SignalBase, k: KData):
    n = self.get_param("n")
    band = self.get_param("band")
    top = (MA(CLOSE, n) + band * STDEV(CLOSE, n))(k)
    bottom = (MA(CLOSE, n) - band * STDEV(CLOSE, n))(k)
    c = k.close
    for i in range(top.discard, len(top)):
        if c[i] > top[i]:
            self._add_buy_signal(k[i].datetime)
        elif c[i] < bottom[i]:
            self._add_sell_signal(k[i].datetime)


def part(n: int = 100, band: float = 0.5) -> SignalBase:
    """
    布林带主要有三条线：中间带 (Middle Band)、以及上下两条边界线，称作上带 (Upper Band) 和下带 (Lower Band)。
    当股价向上突破上界时，为买入信号，当股价向下突破下界时，为卖出信号。

    中轨: MA
    上轨: MA + band * STDEV
    下轨: MA - band * STDEV

    :param int n: 窗口周期
    :param float band: 轨道宽度
    """
    # 实现写法1
    # my_sg = crtSG(bulindai_calculate, params={"n": n, "band": band})
    # return my_sg.clone()

    # 实现写法2
    # return SG_BuLin(n, band)

    # 实现写法3
    ma = MA(CLOSE, n)
    sd = STDEV(CLOSE, n)
    upper = ma + band * sd
    lower = ma - band * sd
    return SG_Band(CLOSE, lower, upper)


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    import sys
    if sys.platform == 'win32':
        import os
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
    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    n = 100
    band = 0.5
    my_sg = get_part(f"{local_hub}.sg.趋势布林带", n=n, band=band)
    print(my_sg)

    if len(sys.argv) <= 1:
        stk = sm['sz000001']
        k = stk.get_kdata(Query(-2000))
        ma = MA(CLOSE, n)
        top = ma + band * STDEV(CLOSE, n)
        top.name = "上轨"
        bottom = ma - band * STDEV(CLOSE, n)
        bottom.name = "下轨"

        k.close.plot(legend_on=True)
        ma(k).plot(new=False, legend_on=True)
        top(k).plot(new=False, legend_on=True)
        bottom(k).plot(new=False, legend_on=True)

        my_sg.to = k
        my_sg.plot(new=False)
        gca().set_title(stk.name)

        import matplotlib.pylab as plt
        plt.show()
