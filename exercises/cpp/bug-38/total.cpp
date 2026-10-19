#include <cstddef>
#include <vector>

int sum_all(const std::vector<int>& values) {
    int total = 0;
    for (std::size_t i = 1; i < values.size(); i++) {
        total += values[i];
    }
    return total;
}
