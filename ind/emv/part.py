
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240526"


def part(n: int = 14) -> Indicator:
    """
    简易波动指标（EMV），是为数不多的考虑价量关系的技术指标。它刻画了股价在下跌的过程当中，由于买气不断的萎靡
    退缩，致使成交量逐渐的减少，EMV 数值也因而尾随下降，直到股价下跌至某一个合理支撑区，捡便宜货的买单促使成
    交量再度活跃，EMV 数值于是作相对反应向上攀升，当EMV 数值由负值向上趋近于零时，表示部分信心坚定的资金，成
    功的扭转了股价的跌势，行情不断反转上扬，并且形成另一次的买进讯号。
    计算方法：
    第一步:
      MID = (TH + TL) / 2 - (YH + YL) / 2
        这里TH 为当天最高价，TL 为当天最低价，YH为前日最高价，YL 为前日最低价。MID > 0意味着今天的平均价高于
        昨天的平均价。
    第二步:
      BRO = VOL/(H-L)
        其中VOL代表交易量，H、L代表同一天的最高价与最低价
    第三步:
      EM = MID/BRO
    第四步:
      EMV = EM 的 N 日简单移动平均

    :param int n: n 日时间窗口, 默认 14 日
    """
    MID = (HIGH + LOW) / 2 - REF((HIGH + LOW) / 2, 1)
    BRO = VOL / (HIGH + LOW)
    EM = MID / BRO
    return MA(EM, n)
