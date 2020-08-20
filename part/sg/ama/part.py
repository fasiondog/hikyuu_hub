from hikyuu import SG_Single, AMA

# 部件作者
author = "fasiondog"

# 简要描述
brief = """AMA信号指示器
使用《精明交易者》 [BOOK1]_ 中给出的曲线拐点算法判断曲线趋势，公式见下::

    filter = percentage * STDEV((AMA-AMA[1], N)

    Buy  When AMA - AMA[1] > filter
    or Buy When AMA - AMA[2] > filter
    or Buy When AMA - AMA[3] > filter 
"""

# 详细信息
details = ""

# 参数要求及默认值
params = (('filter_n', 'int', 10, '过滤窗口周期'), ('filter_p', 'float', 0.1, '转折判断阈值'))

sg = SG_Single(AMA())

if __name__ == '__main__':
    print(sg)