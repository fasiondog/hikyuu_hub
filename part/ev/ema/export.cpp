
/*
 *  Created on: 20240222
 *      Author: fasiondog
 */

#include <pybind11/pybind11.h>
#include <hikyuu/hikyuu.h>

using namespace hku;
namespace py = pybind11;

void export_part(py::module& m) {
    m.def("my_part",
          [](int n, const string& market) { return EV_Bool(CLOSE() > EMA(CLOSE(), n), market); });
}
