from hikyuu import SP_FixedPercent

# 部件作者
author = "fasiondog"

# 版本
version = '20200824'

# 帮助信息
doc = """
固定百分比移滑价差算法

买入实际价格 = 计划买入价格 * (1 + p)，卖出实际价格 = 计划卖出价格 * (1 - p)

参数
- (float) percent = 0.001 : 偏移的固定比例
"""

def part(percent=0.001)
    return SP_FixedPercent(percent)

if __name__ == '__main__':
    print(sg)