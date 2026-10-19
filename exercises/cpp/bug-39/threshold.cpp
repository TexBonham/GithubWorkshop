#include <vector>

int count_above(const std::vector<int>& readings, int limit) {
    int count = 0;
    for (int r : readings) {
        if (r >= limit) {
            count++;
        }
    }
    return count;
}
