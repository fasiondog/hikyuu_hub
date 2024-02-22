
#!/usr/bin/python
# -*- coding: utf8 -*-

import sys

try:
    if sys.version_info[1] == 8:
        try:
            from .export38 import *
        except:
            from export38 import *
    elif sys.version_info[1] == 9:
        try:
            from .export39 import *
        except:
            from export39 import *
    elif sys.version_info[1] == 10:
        try:
            from .export310 import *
        except:
            from export310 import *    
    elif sys.version_info[1] == 11:
        try:
            from .export311 import *
        except:
            from export311 import *    
    elif sys.version_info[1] == 12:
        try:
            from .export312 import *
        except:
            from export312 import *
    else:
        try:
            from .export import *
        except:
            from export import *
except:
    try:
        from .export import *
    except:
        from export import *
