
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240514"


def part(ind: Indicator, bottomn: int = 2):
    """
    选取因子值最低的 bottomn 支证券, 使用前，需要先使用 prepare 设置相关参数

    :param Indicator ind: 单因子
    :param int bottomn: 选取因子值最低的 bottomn 支证券
    """
    my_se = SE_MultiFactor([REF(ind, 1)], topn=bottomn, mode="MF_EqualWeight")
    my_se.set_param("reverse", True)
    return my_se
