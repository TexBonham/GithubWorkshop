#include <cassert>
#include <iostream>
#include <string>

#include "reverse.cpp"

int main() {
    assert(reverse_text("abc") == "cba");
    assert(reverse_text("") == "");
    assert(reverse_text("a") == "a");
    assert(reverse_text("hello") == "olleh");
    std::cout << "All reverse_text() tests passed" << std::endl;
    return 0;
}
