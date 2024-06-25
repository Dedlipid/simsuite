cmake_minimum_required(VERSION 3.10)
project(SimSuite_CPP CXX)

set(CMAKE_CXX_STANDARD 11)

# Add integrators and systems libraries
add_library(integrators_cpp src/integrators.cpp)
add_library(systems_cpp src/systems.cpp)

# Add executable
add_executable(main_cpp src/main.cpp)

# Link libraries
target_link_libraries(main_cpp integrators_cpp systems_cpp)
