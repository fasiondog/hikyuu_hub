
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240501"


def part():
    """获取静态市盈率"""
    EPS = FINANCE(0)
    EPS.set_param("only_year_report", True)
    PE = CLOSE / EPS
    PE.name = "静态市盈率"
    return PE
