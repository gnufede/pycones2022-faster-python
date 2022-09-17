#include "cystring.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

// namespace py = pybind11;

PYBIND11_MODULE(pybind11string, m) {
  m.doc() = "pybind11 example plugin"; // optional module docstring

  m.def("cfind_user_agent_header", &cystring::find_user_agent_header, "Doc");
}
