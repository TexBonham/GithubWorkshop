#include <cassert>
#include <cmath>
#include <iostream>

#include "temperature.cpp"

static bool close(double a, double b) {
    return std::fabs(a - b) < 1e-9;
}

int main() {
    assert(close(celsius_to_fahrenheit(100), 212.0));
    assert(close(celsius_to_fahrenheit(0), 32.0));
    assert(close(celsius_to_fahrenheit(-40), -40.0));
    assert(close(celsius_to_fahrenheit(37), 98.6));
    std::cout << "All celsius_to_fahrenheit() tests passed" << std::endl;
    return 0;
}
