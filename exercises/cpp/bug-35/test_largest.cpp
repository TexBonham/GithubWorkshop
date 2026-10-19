#include <cassert>
#include <iostream>
#include <vector>

#include "largest.cpp"

int main() {
    assert(largest({3, 9, 4}) == 9);
    assert(largest({7}) == 7);
    assert(largest({-5, -2, -9}) == -2);
    assert(largest({0, -1}) == 0);
    std::cout << "All largest() tests passed" << std::endl;
    return 0;
}
