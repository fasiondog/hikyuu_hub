
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240528"


def part() -> list:
    """获取沪深300股票列表"""
    return [s for s in sm.get_block("指数板块", "沪深300")]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    from hikyuu.interactive import *

    ind = part()
    print(ind)
