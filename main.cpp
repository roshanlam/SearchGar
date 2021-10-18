#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <chrono>
#include <thread>
#include <iostream>
#include <string>
#include <fstream>

namespace py = pybind11;

float some_fn(float arg1, float arg2) {
  return arg1 + arg2;
}

void openFile(std::string filename){
    std::ofstream MyFile("Data.txt");
    MyFile << "Data";
    MyFile.close();
}

PYBIND11_MODULE(module_name, module_handle) {
  module_handle.doc() = "I'm a docstring hehe";
  module_handle.def("some_fn_python_name", &some_fn);
  module_handle.def("openFile", &openFile);
}
