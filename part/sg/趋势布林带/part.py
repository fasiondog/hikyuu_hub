
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
    当股价向上突破上界时，为卖出信号，当股价向下突破下界时，为买入信号。

    中轨: MA
    上轨: MA + band * STDEV
    下轨: MA - band * STDEV

    :param int n: 窗口周期
    :param float band: 轨道宽度
    """
    # my_sg = crtSG(bulindai_calculate, params={"n": n, "band": band})
    # return my_sg.clone()
    # return SG_BuLin(n, band)
    ma = MA(CLOSE, n)
    sd = STDEV(CLOSE, n)
    upper = ma + band * sd
    lower = ma - band * sd
    return SG_Band(CLOSE, lower, upper)
