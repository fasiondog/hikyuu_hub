
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240509"


def part(bottomn: int = 2):
    """
    选取市净率最低的 bottomn 支证券, 使用前，需要先使用 prepare 设置相关参数

    :param int bottomn: 最低 bottomn 支证券
    """
    市净率 = get_part("default.ind.市净率")
    local_hub = get_current_hub(__file__)
    return get_part(f"{local_hub}.se.最低单因子", ind=市净率, bottomn=bottomn)
