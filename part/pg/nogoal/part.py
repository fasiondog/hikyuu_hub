from hikyuu import PG_NoGoal

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part():
    return PG_NoGoal()


part.__doc__ = PG_NoGoal.__doc__

if __name__ == '__main__':
    print(part())