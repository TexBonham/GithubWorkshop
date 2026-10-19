#include <cassert>
#include <iostream>
#include <vector>

#include "total.cpp"

int main() {
    assert(sum_all({1, 2, 3}) == 6);
    assert(sum_all({10}) == 10);
    assert(sum_all({}) == 0);
    assert(sum_all({-4, 4, 5}) == 5);
    std::cout << "All sum_all() tests passed" << std::endl;
    return 0;
}
