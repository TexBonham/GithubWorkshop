#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

#include "sensor.cpp"

static bool close(double a, double b) {
    return std::fabs(a - b) < 1e-9;
}

int main() {
    assert(close(average_reading({1, 2}), 1.5));
    assert(close(average_reading({10, 20, 30}), 20.0));
    assert(close(average_reading({3, 4, 4}), 11.0 / 3.0));
    assert(close(average_reading({5}), 5.0));
    assert(close(average_reading({}), 0.0));
    std::cout << "All average_reading() tests passed" << std::endl;
    return 0;
}
