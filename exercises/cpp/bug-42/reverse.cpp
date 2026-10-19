#include <string>

std::string reverse_text(const std::string& s) {
    std::string out;
    for (int i = static_cast<int>(s.size()) - 1; i > 0; i--) {
        out += s[i];
    }
    return out;
}
