from hikyuu import AMA, CLOSE

# 部件作者
author = "fasiondog"

# 版本
version = '20231025'


def part(n=10, fast_n=2, slow_n=30):
    """test
    """
    return AMA(n=n, fast_n=fast_n, slow_n=slow_n)


if __name__ == '__main__':
    print(part())