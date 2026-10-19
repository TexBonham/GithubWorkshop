#include <cassert>
#include <iostream>
#include <string>

#include "counter.cpp"

int main() {
    assert(count_char("banana", 'a') == 3);
    assert(count_char("banana", 'z') == 0);
    assert(count_char("", 'a') == 0);
    assert(count_char("aAa", 'a') == 2);
    std::cout << "All count_char() tests passed" << std::endl;
    return 0;
}
