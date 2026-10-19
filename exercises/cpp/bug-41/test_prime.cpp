#include <cassert>
#include <iostream>

#include "prime.cpp"

int main() {
    assert(!is_prime(0));
    assert(!is_prime(1));
    assert(is_prime(2));
    assert(is_prime(13));
    assert(!is_prime(9));
    std::cout << "All is_prime() tests passed" << std::endl;
    return 0;
}
