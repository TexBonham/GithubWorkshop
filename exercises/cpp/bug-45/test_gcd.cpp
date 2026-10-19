#include <cassert>
#include <iostream>

#include "gcd.cpp"

int main() {
    assert(gcd(12, 18) == 6);
    assert(gcd(7, 13) == 1);
    assert(gcd(10, 0) == 10);
    assert(gcd(100, 25) == 25);
    std::cout << "All gcd() tests passed" << std::endl;
    return 0;
}
