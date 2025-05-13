
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
    my_se = SE_MultiFactor([ind], topn=bottomn, mode="MF_EqualWeight")
    my_se.set_param("reverse", True)
    return my_se


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    import sys
    if sys.platform == 'win32':
        import os
        os.system('chcp 65001')

    from hikyuu.interactive import *
    try:
        from .part import *
    except:
        from part import *

    # 请在下方编写测试代码
    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    my_se = get_part(f"{local_hub}.se.最低单因子", ind=ROC(CLOSE))
    print(my_se)
