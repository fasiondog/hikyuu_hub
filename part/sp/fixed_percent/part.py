from hikyuu import SP_FixedPercent

# 部件作者
author = "fasiondog"

# 版本
version = '20200824'


def part(p=0.001):
    return SP_FixedPercent(p)


part.__doc__ = SP_FixedPercent.__doc__

if __name__ == '__main__':
    print(part())