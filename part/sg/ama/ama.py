from hikyuu import SG_Single

name = "SG_AMA"
author = "fasiondog"
doc = """AMA信号指示器
使用《精明交易者》 [BOOK1]_ 中给出的曲线拐点算法判断曲线趋势，公式见下::

    filter = percentage * STDEV((AMA-AMA[1], N)

    Buy  When AMA - AMA[1] > filter
    or Buy When AMA - AMA[2] > filter
    or Buy When AMA - AMA[3] > filter 
"""

params = (('filter_n', 'int', 10), ('filter_p', 'float', 0.1))

sg = SG_Single(AMA())
