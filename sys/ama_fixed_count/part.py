import hikyuu as hku

# 部件作者
author = "fasiondog"

# 版本
version = '20200826'


def part(filter_n=20, filter_p=0.1, ama_n=10, ama_fast_n=2, ama_slow_n=30, fixed_count=100):
    """ 使用AMA信号，每次买固定数量

    :param int filter_n: 曲线拐点计算窗口
    :param float filter_p: 曲线拐点计算百分比
    :param int ama_n: AMA窗口周期
    :param int ama_fast_n: AMA快线窗口周期
    :param int ama_slow_n: AMA慢线窗口周期
    :param int fixed_count: 每次固定买入的数量
    """
    house = hku.get_current_hub(__file__)
    sg = hku.get_part(
        "{}.sg.ama".format(house),
        filter_n=filter_n,
        filter_p=filter_p,
        ama_n=ama_n,
        ama_fast_n=ama_fast_n,
        ama_slow_n=ama_slow_n
    )
    mm = hku.get_part('{}.mm.fixed_count'.format(house), n=fixed_count)
    sys = hku.SYS_Simple(sg=sg, mm=mm)
    return sys


if __name__ == '__main__':
    print(part())