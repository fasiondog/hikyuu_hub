
/*
 *  Created on: {today}
 *      Author: {user}
 */

#include <pybind11/pybind11.h>
#include <hikyuu/hikyuu.h>

using namespace hku;
namespace py = pybind11;

void export_part(py::module& m) {
    m.def("my_part", [](int n) { return CN_Bool(CLOSE() > MA(CLOSE(), n)); });
}
