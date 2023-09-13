/**
 * C++ programm utilizing memoization to calculate the Fibonacci sequence.
 *
 * @File = fibonacci.cpp
 * @Date = 2023-09-13
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <iostream>

/* calculate the n-th Fibonacci number */
long long fibonacci(int n) {
    long long fib[n + 2];

    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    return fib[n];
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    int n = atoi(argv[1]);
    if (n < 0) {
        std::cout << "Number must be positive." << std::endl;
        return 1;
    }

    std::cout << fibonacci(n) << std::endl;
    return 0;
}
