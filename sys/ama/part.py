import hikyuu as hku

# 部件作者
author = "fasiondog"

# 版本
version = '20200826'


def part(filter_n=20, filter_p=0.1, ama_n=10, ama_fast_n=2, ama_slow_n=30):
    house = hku.get_current_house(__file__)
    sg = hku.get_part(
        "{}.sg.ama".format(house),
        filter_n=filter_n,
        filter_p=filter_p,
        ama_n=ama_n,
        ama_fast_n=ama_fast_n,
        ama_slow_n=ama_slow_n
    )
    mm = hku.get_part('{}.mm.fixed_count'.format(house), n=100)
    sys = hku.SYS_Simple(sg=sg, mm=mm)
    return sys


if __name__ == '__main__':
    print(part())