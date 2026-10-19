#include <cassert>
#include <cmath>
#include <iostream>

#include "current.cpp"

static bool close(double a, double b) {
    return std::fabs(a - b) < 1e-9;
}

int main() {
    assert(close(current(10, 5), 2.0));
    assert(close(current(12, 4), 3.0));
    assert(close(current(5, 10), 0.5));
    assert(close(current(0, 3), 0.0));
    std::cout << "All current() tests passed" << std::endl;
    return 0;
}
