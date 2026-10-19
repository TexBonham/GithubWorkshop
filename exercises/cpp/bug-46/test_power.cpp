#include <cassert>
#include <iostream>

#include "power.cpp"

int main() {
    assert(power(2, 3) == 8);
    assert(power(5, 0) == 1);
    assert(power(3, 1) == 3);
    assert(power(10, 4) == 10000);
    std::cout << "All power() tests passed" << std::endl;
    return 0;
}
