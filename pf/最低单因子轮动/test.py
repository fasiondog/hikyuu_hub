
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu.interactive import *
try:
    from .part import *
except:
    from part import *

import sys
if sys.platform == 'win32':
    import os
    os.system('chcp 65001')

if __name__ == "__main__":
    pass
