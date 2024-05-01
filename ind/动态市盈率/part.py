
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240501"


def part():
    """动态市盈率"""
    EPS = FINANCE(0)
    EPS.set_param("dynamic", True)
    PE = CLOSE / EPS
    PE.name = "动态态市盈率"
    return PE
