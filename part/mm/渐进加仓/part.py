#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(tier_count: int = 5, tier_size: int = 100):
    """
    SMA 偏离渐进加仓 MM

    按 tier_count 档、每档 tier_size 股买入；卖出信号触发时全平所有持仓。
    支持连续多次买入（渐进加仓），配合 alternate=False 的信号使用。

    :param tier_count: 最大加仓档位
    :param tier_size: 每档买入股数
    :return: part instance
    """
    buy_counts = [tier_size] * tier_count
    ret = MM_FixedCountTps(buy_counts, [])
    ret.name = "渐进加仓MM"
    return ret


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
    mm = part()
    print(mm)
