/**
 * Recursive C++ programm to calculate the factorial of a given number.
 *
 * @File = factorial.cpp
 * @Date = 2023-09-10
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <iostream>

/* calculate the factorial of a given number */
long long factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

/* main function */
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

    std::cout << factorial(n) << std::endl;
    return 0;
}
