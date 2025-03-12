from hikyuu import AF_EqualWeight

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part():
    return AF_EqualWeight()


part.__doc__ = AF_EqualWeight.__doc__


if __name__ == '__main__':
    print(part())
