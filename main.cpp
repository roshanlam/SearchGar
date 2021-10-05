#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <chrono>
#include <thread>

namespace py = pybind11;

float some_fn(float arg1, float arg2) {
  return arg1 + arg2;
}

class SomeClass {
  float multiplier;
public:
  SomeClass(float multiplier_) : multiplier(multiplier_) {};

  float multiply(float input) {
    return multiplier * input;
  }

  std::vector<float> multiply_list(std::vector<float> items) {
    for (auto i = 0; i < items.size(); i++) {
      items[i] = multiply(items.at(i));
    }
    return items;
  }

  // py::tuple multiply_two(float one, float two) {
  //   return py::make_tuple(multiply(one), multiply(two));
  // }

  std::vector<std::vector<uint8_t>> make_image() {
    auto out = std::vector<std::vector<uint8_t>>();
    for (auto i = 0; i < 128; i++) {
      out.push_back(std::vector<uint8_t>(64));
    }
    for (auto i = 0; i < 30; i++) {
      for (auto j = 0; j < 30; j++) { out[i][j] = 255; }
    }
    return out;
  }

  void set_mult(float val) {
    multiplier = val;
  }

  float get_mult() {
    return multiplier;
  }

  void function_that_takes_a_while() {
    py::gil_scoped_release release;
    std::cout << "starting" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(2000));
    std::cout << "ended" << std::endl;

    // py::gil_scoped_acquire acquire;
    // auto list = py::list();
    // list.append(1);
  }
};

SomeClass some_class_factory(float multiplier) {
  return SomeClass(multiplier);
}


PYBIND11_MODULE(module_name, module_handle) {
  module_handle.doc() = "I'm a docstring hehe";
  module_handle.def("some_fn_python_name", &some_fn);
  module_handle.def("some_class_factory", &some_class_factory);
  py::class_<SomeClass>(
			module_handle, "PySomeClass"
			).def(py::init<float>())
    .def_property("multiplier", &SomeClass::get_mult, &SomeClass::set_mult)
    .def("multiply", &SomeClass::multiply)
    .def("multiply_list", &SomeClass::multiply_list)
    // .def_property_readonly("image", &SomeClass::make_image)
    .def_property_readonly("image", [](SomeClass &self) {
				      py::array out = py::cast(self.make_image());
				      return out;
				    })
    // .def("multiply_two", &SomeClass::multiply_two)
    .def("multiply_two", [](SomeClass &self, float one, float two) {
			   return py::make_tuple(self.multiply(one), self.multiply(two));
			 })
    .def("function_that_takes_a_while", &SomeClass::function_that_takes_a_while)
    ;
}
