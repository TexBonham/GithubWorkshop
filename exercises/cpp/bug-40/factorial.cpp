long long factorial(int n) {
    long long result = 0;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
