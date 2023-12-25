cmake_minimum_required(VERSION 3.5)

find_package(PythonLibs ${PY_VERSION} REQUIRED)
find_package(Boost REQUIRED COMPONENTS python3)

add_library(classes SHARED classes.cpp)

target_include_directories(classes PRIVATE ${Python3_INCLUDE_DIRS})
set_target_properties(classes PROPERTIES PREFIX "")

target_link_libraries(classes
    ${Boost_LIBRARIES}
    )

    install(TARGETS classes DESTINATION lib)