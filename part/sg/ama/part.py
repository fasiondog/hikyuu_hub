from hikyuu import SG_Single, AMA, CLOSE

# 部件作者
author = "fasiondog"

# 版本
version = '20200824'


def part(filter_n=20, filter_p=0.1, ama_n=10, ama_fast_n=2, ama_slow_n=30):
    """AMA信号指示器
    使用《精明交易者》 [BOOK1]_ 中给出的曲线拐点算法判断曲线趋势，公式见下::

        filter = percentage * STDEV((AMA-AMA[1], N)

        Buy  When AMA - AMA[1] > filter
        or Buy When AMA - AMA[2] > filter
        or Buy When AMA - AMA[3] > filter

    :param int filter_n: 
    :param float filter_p:
    """
    return SG_Single(AMA(CLOSE(), ama_n, ama_fast_n, ama_slow_n), filter_n=filter_n, filter_p=filter_p)


if __name__ == '__main__':
    print(part())