#include <iostream>
#include <vector>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    std::vector<bool> primes(100000001, false);
    
    for (long long i = 2; i <= sqrt(n); i++) {
        if (!primes[i]) {
            for (long long j = 2 * i; j <= n; j += i) {
                primes[j] = true;
            }
        }
    }

    long long res = 1;
    for (long long i = 2; i <= n; i++) {
        if (!primes[i]) {
            long long temp = 1;
            while (temp * i <= n) {
                temp *= i;
                temp %= 4294967296;
            }
            res *= temp;
            res %= 4294967296;
        }
    }

    std::cout << res << std::endl;
    return 0;
}

