#include <vector>

int largest(const std::vector<int>& values) {
    int best = 0;
    for (int v : values) {
        if (v > best) {
            best = v;
        }
    }
    return best;
}
