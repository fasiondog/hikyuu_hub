from hikyuu import SE_Fixed

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part():
    return SE_Fixed()


part.__doc__ = SE_Fixed.__doc__

if __name__ == '__main__':
    print(part())