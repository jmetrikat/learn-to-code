/**
 * C++ programm to calculate all prime numbers up to a given number.
 *
 * @File = primes.cpp
 * @Date = 2023-10-28
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <iostream>

/* calculate primes using the sieve of eratosthenes */
void primes(int n) {
    int *is_prime = new int[n + 1];

    for (int i = 0; i <= n; i++) {
        is_prime[i] = 1;
    }

    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            std::cout << i << std::endl;
        }
    }

    return;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    int n = atoi(argv[1]);
    if (n < 2) {
        std::cout << "Number must be greater than 1." << std::endl;
        return 1;
    }

    primes(n);
    return 0;
}
