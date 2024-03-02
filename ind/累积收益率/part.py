from hikyuu import *

# 部件作者
author = "fasiondog"

# 版本
version = '20231223'


def part():
    """
    累积收益率 (Cumulative return)

    示例: 
        ind = get_part('default.ind.累积收益率')
        k = get_kdata('sz000001', Query(-200))
        x = ind(k.close)
        x.plot()
    """
    return ROCP(0) + 1


if __name__ == '__main__':
    from hikyuu.interactive import *
    import matplotlib.pylab as plt
    k = get_kdata("sz000001", Query(-300))
    ind = part()
    f = create_figure(2)
    k.plot(axes=f[0])
    ind(k.close).plot(axes=f[1])
    plt.show()
