#include <cassert>
#include <iostream>
#include <vector>

#include "threshold.cpp"

int main() {
    assert(count_above({1, 5, 10, 15}, 10) == 1);
    assert(count_above({5, 5, 5}, 5) == 0);
    assert(count_above({}, 3) == 0);
    assert(count_above({-1, 0, 1}, -2) == 3);
    std::cout << "All count_above() tests passed" << std::endl;
    return 0;
}
