#include <cstddef>
#include <vector>

int index_of_min(const std::vector<int>& values) {
    std::size_t best = 0;
    for (std::size_t i = 1; i < values.size(); i++) {
        if (values[i] > values[best]) {
            best = i;
        }
    }
    return static_cast<int>(best);
}
