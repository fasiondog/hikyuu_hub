
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu.interactive import *
try:
    from .part import *
except:
    from part import *


if __name__ == '__main__':
    from hikyuu.interactive import *
    import matplotlib.pylab as plt
    k = get_kdata("sz000001", Query(-300))
    ind = part()
    print(ind)

    if len(sys.argv) > 1:
        ind(k).plot()
        plt.show()
