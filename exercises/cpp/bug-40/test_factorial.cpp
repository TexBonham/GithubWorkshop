#include <cassert>
#include <iostream>

#include "factorial.cpp"

int main() {
    assert(factorial(0) == 1);
    assert(factorial(1) == 1);
    assert(factorial(5) == 120);
    assert(factorial(6) == 720);
    std::cout << "All factorial() tests passed" << std::endl;
    return 0;
}
