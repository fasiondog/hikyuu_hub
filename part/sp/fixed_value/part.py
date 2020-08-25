from hikyuu import SP_FixedValue

# 部件作者
author = "fasiondog"

# 版本
version = '20200824'


def part(value=0.01):
    return SP_FixedValue(value)


part.__doc__ = SP_FixedValue.__doc__

if __name__ == '__main__':
    print(part())