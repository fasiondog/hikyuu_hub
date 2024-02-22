
#include <pybind11/pybind11.h>
#include <hikyuu/hikyuu.h>

using namespace hku;
namespace py = pybind11;

void export_part(py::module& m);

#if PY_MINOR_VERSION == 8
PYBIND11_MODULE(export38, m) {
#elif PY_MINOR_VERSION == 9
PYBIND11_MODULE(export39, m) {
#elif PY_MINOR_VERSION == 10
PYBIND11_MODULE(export310, m) {
#elif PY_MINOR_VERSION == 11
PYBIND11_MODULE(export311, m) {
#elif PY_MINOR_VERSION == 12
PYBIND11_MODULE(export312, m) {
#elif PY_MINOR_VERSION == 13
PYBIND11_MODULE(export313, m) {
#else
PYBIND11_MODULE(export, m) {
#endif
    export_part(m);
}
