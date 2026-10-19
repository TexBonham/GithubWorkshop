#include <cassert>
#include <cmath>
#include <iostream>

#include "kinetic_energy.cpp"

bool close(double a, double b) {
    return std::fabs(a - b) < 1e-9;
}

int main() {
    assert(close(kinetic_energy(2.0, 3.0), 9.0));
    assert(close(kinetic_energy(1.0, 1.0), 0.5));
    assert(close(kinetic_energy(10.0, 0.0), 0.0));
    assert(close(kinetic_energy(4.0, -2.0), 8.0));
    std::cout << "All kinetic_energy() tests passed" << std::endl;
    return 0;
}
