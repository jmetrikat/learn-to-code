/**
 * C++ program to calculate prime factors of a given number.
 *
 * @File = primefactors.cpp
 * @Date = 2023-10-28
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <iostream>

/* calculate prime factors of a given number */
void primeFactors(int n) {
    int found_factor = 0;

    for (int i = 2; i < n; i++) {
        int is_prime = 1;

        for (int j = 2; j < i; j++) {
            if (i % j == 0) {
                is_prime = 0;
                break;
            }
        }

        if (n % i == 0 && is_prime) {
            std::cout << i << std::endl;
            found_factor = 1;
        }

    }

    if (!found_factor) {
        std::cout << n << " is prime." << std::endl;
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

    primeFactors(n);
    return 0;
}
