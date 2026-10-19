#include <string>

int count_char(const std::string& text, char target) {
    int count = 0;
    for (char c : text) {
        if (c == target) {
            count++
        }
    }
    return count;
}
