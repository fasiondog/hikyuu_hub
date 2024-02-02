
/*
 *  Created on: 20240202
 *      Author: fasiondog
 */

#include <pybind11/pybind11.h>
#include <hikyuu/hikyuu.h>

using namespace hku;
namespace py = pybind11;

void export_part(py::module& m) {
    m.def("my_part", [](int n, int fast_n, int slow_n) {
        return CN_Bool(CLOSE() > AMA(CLOSE(), n, fast_n, slow_n));
    });
}
