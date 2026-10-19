#include <cassert>
#include <iostream>
#include <vector>

#include "minimum.cpp"

int main() {
    assert(index_of_min({4, 2, 9}) == 1);
    assert(index_of_min({1, 2, 3}) == 0);
    assert(index_of_min({5, 3, 1}) == 2);
    assert(index_of_min({7}) == 0);
    std::cout << "All index_of_min() tests passed" << std::endl;
    return 0;
}
