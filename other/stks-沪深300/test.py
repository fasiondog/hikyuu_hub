
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
if sys.platform == 'win32':
    import os
    os.system('chcp 65001')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    from hikyuu.interactive import *
    try:
        from .part import *
    except:
        from part import *

    ind = part()
    print(ind)
