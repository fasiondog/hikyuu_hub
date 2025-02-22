
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(n: int = 1):
    """
    对数收益率

    :param int n: 默认为1
    """
    ret = LN(CLOSE() / REF(CLOSE(), n))
    ret.name = "对数收益率"
    return ret
