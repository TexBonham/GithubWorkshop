#include <cassert>
#include <iostream>

#include "leap.cpp"

int main() {
    assert(is_leap_year(2024));
    assert(!is_leap_year(2023));
    assert(!is_leap_year(1900));
    assert(is_leap_year(2000));
    std::cout << "All is_leap_year() tests passed" << std::endl;
    return 0;
}
