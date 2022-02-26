from hikyuu import AF_FixedWeight

# 部件作者
author = "fasiondog"

# 版本
version = '20220226'


def part(weight=0.1):
    return AF_FixedWeight(weight)


part.__doc__ = AF_FixedWeight.__doc__

if __name__ == '__main__':
    print(part())