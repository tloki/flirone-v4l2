cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(flironeProject VERSION 0.1)

# set C language standard
SET(CMAKE_C_STANDARD 99)

# find LibUSB library to link to
find_path(LIBUSB_INCLUDE_DIR
        NAMES libusb.h
        PATH_SUFFIXES "include" "libusb" "libusb-1.0")
find_library(LIBUSB_LIBRARY
        NAMES usb
        PATH_SUFFIXES "lib" "lib32" "lib64")

# add executable
add_executable(flirone src/flirone.c)
add_executable(flirone_stock src/flirone_stock.c)

#
target_include_directories(flirone PRIVATE src ${LIBUSB_INCLUDE_DIR})
target_link_libraries(flirone usb-1.0 ${LIBUSB_LIBRARY} m)

target_include_directories(flirone_stock PRIVATE src ${LIBUSB_INCLUDE_DIR})
target_link_libraries(flirone_stock usb-1.0 ${LIBUSB_LIBRARY} m)