#include <vector>

double average_reading(const std::vector<int>& values) {
    if (values.empty()) {
        return 0.0;
    }
    int total = 0;
    for (int v : values) {
        total += v;
    }
    return total / static_cast<int>(values.size());
}
