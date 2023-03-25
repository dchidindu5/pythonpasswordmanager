cmake_minimum_required(VERSION 3.0)

project(password_manager)

set(CMAKE_CXX_STANDARD 11)

add_executable(password_manager password_manager.py)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

target_link_libraries(password_manager PRIVATE Python3::Python Python3::Module)
