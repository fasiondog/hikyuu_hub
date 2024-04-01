
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
    # f = create_figure(2)
    # k.plot(axes=f[0])
    # ind(k).plot(axes=f[1])
    # plt.show()
