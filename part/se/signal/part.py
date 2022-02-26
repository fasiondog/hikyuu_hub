from hikyuu import SE_Signal

# 部件作者
author = "fasiondog"

# 版本
version = '20220226'


def part():
    return SE_Signal()


part.__doc__ = SE_Signal.__doc__

if __name__ == '__main__':
    print(part())