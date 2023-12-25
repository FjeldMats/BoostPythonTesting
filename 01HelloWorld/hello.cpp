#include <iostream>
#include <string>
#include <boost/python.hpp>
#include <boost/python/str.hpp>
#include <boost/python/extract.hpp>

char const *greet(boost::python::str name)
{
    std::string s = boost::python::extract<std::string>(name);

    std::cout << "Hello World, " << s << "!\n";
}

char const *greet2()
{
    return "Hello, World2!";
}

BOOST_PYTHON_MODULE(hello)
{
    using namespace boost::python;
    def("greet", greet);
    def("greet2", greet2);
}