cmake_minimum_required(VERSION 3.5)

find_package(PythonLibs ${PY_VERSION} REQUIRED)
find_package(Boost REQUIRED COMPONENTS python3)

add_library(hello SHARED hello.cpp)

target_include_directories(hello PRIVATE ${Python3_INCLUDE_DIRS})
set_target_properties(hello PROPERTIES PREFIX "")

target_link_libraries(hello
    ${Boost_LIBRARIES}
    )

    install(TARGETS hello DESTINATION lib)