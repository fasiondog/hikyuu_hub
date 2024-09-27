
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240601"


def part():
    """获取所有ETF"""
    return [s for s in sm if s.type == constant.STOCKTYPE_ETF]
