cmake_minimum_required(VERSION 3.10)
project(SimSuite_C C)

set(CMAKE_C_STANDARD 99)

# Add integrators and systems libraries
add_library(integrators src/integrators.c)
add_library(systems src/systems.c)

# Add executable
add_executable(main_c src/main.c)

# Link libraries and math library
target_link_libraries(main_c integrators systems m)
