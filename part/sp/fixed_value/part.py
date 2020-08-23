from hikyuu import SP_FixedValue

# 部件作者
author = "fasiondog"

# 版本
version = '20200824'

# 帮助信息
doc = """
固定价格移滑价差算法

买入实际价格 = 计划买入价格 + 偏移价格，卖出实际价格 = 计划卖出价格 - 偏移价格

参数
- value (float) : 偏移价格， 默认值 0.01
"""

part = SP_FixedValue()

if __name__ == '__main__':
    print(sg)