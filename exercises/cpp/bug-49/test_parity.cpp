#include <cassert>
#include <iostream>

#include "parity.cpp"

int main() {
    assert(is_even(4));
    assert(!is_even(7));
    assert(is_even(0));
    assert(!is_even(-3));
    assert(is_even(-2));
    std::cout << "All is_even() tests passed" << std::endl;
    return 0;
}
