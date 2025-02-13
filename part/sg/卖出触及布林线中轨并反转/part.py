
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250214"


def part(n: int = 20, band=2.0):
    """
    布林线和常见的看跌 K 线形态（以射击之星为例）作为卖出信号。射击之星的特征是上影线较长，实体较小，且通常出现在上涨趋势中。
    射击之星判断条件:
    ShootingStar:=HIGH - MAX(CLOSE,OPEN) >= 2 * ABS(CLOSE - OPEN) AND MIN(CLOSE,OPEN) - LOW <= ABS(CLOSE - OPEN) / 2;
    卖出信号：触及上轨且出现射击之星
    SellSignal: CLOSE >= UPPER AND ShootingStar;
    """
    local_hub = get_current_hub(__file__)
    boll = get_part(f"{local_hub}.ind.布林线", n=n, band=band)
    upper = RESULT(boll, 1)
    射击之星 = get_part(f"{local_hub}.ind.射击之星")
    sg = SG_OneSide((CLOSE() >= upper) & 射击之星, False)
    sg.name = "卖出触及布林线中轨并反转"
    return sg
