#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(rsi_n: int = 2, buy_th: float = 25.0, n: int = 50, use_ma_filter: bool = True):
    """
    RSI oversold reversal buy signal with optional MA trend filter.

    Calculation:
        rsi = RSI(CLOSE, rsi_n)
        ma  = MA(CLOSE, n)

    Entry fires when the previous bar's RSI is below the oversold threshold and
    the current RSI turns up (a reversal confirmation), and — when the MA filter
    is enabled — only if the close is above the MA.

        cond = (RSI[1] < buy_th) & (RSI > RSI[1])
        if use_ma_filter: cond &= (CLOSE > MA)

    :param rsi_n: RSI period
    :param buy_th: RSI oversold entry threshold
    :param n: MA trend-filter period
    :param use_ma_filter: whether to require close above the MA
    :return: part instance
    """

    def calculate(self, k):
        rsi = RSI(CLOSE(k), rsi_n)
        ma = MA(CLOSE(k), n)
        for i in range(max(ma.discard, rsi.discard) + 1, len(k)):
            rsi_prev = rsi[i - 1]
            rsi_cur = rsi[i]
            if rsi_prev < buy_th and rsi_cur > rsi_prev:
                if use_ma_filter and not (k[i].close > ma[i]):
                    continue
                self._add_buy_signal(k[i].datetime)

    sg = crtSG(calculate,
               params={"rsi_n": rsi_n, "buy_th": buy_th, "n": n, "use_ma_filter": use_ma_filter},
               name="买入RSI超卖反转")
    sg.set_param("alternate", False)
    return sg


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
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

    # 请在下方编写测试代码
    sg = part()
    print(sg)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-500))
    sg.to = k

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    MA(CLOSE, n=n)(k).plot(new=False, axes=ax1)
    RSI(CLOSE, rsi_n)(k).plot(axes=ax2)
    sg.plot(new=False, axes=ax2)
    plt.show()
