cmake_minimum_required(VERSION 3.5)

find_package(PythonLibs ${PY_VERSION} REQUIRED)
find_package(Boost REQUIRED COMPONENTS python3)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")

add_library(pyprime SHARED pyprime.cpp)

target_include_directories(pyprime PRIVATE ${Python3_INCLUDE_DIRS})
set_target_properties(pyprime PROPERTIES PREFIX "")

target_link_libraries(pyprime
    ${Boost_LIBRARIES}
    )

    install(TARGETS pyprime DESTINATION lib)
