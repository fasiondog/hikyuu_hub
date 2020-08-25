from hikyuu import MM_FixedPercent

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(p=0.03):
    return MM_FixedPercent(p)


part.__doc__ = MM_FixedPercent.__doc__

if __name__ == '__main__':
    print(part())