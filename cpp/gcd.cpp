/**
 * Recursive C++ program to calculate the greatest common divisor of two given numbers.
 *
 * @File = gcd.cpp
 * @Date = 2023-10-28
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <iostream>

/* calculate the greatest common divisor using euclid's algorithm */
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }

    return gcd(b, a % b);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cout << "Usage: " << argv[0] << " <number> <number>" << std::endl;
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    std::cout << gcd(abs(a), abs(b)) << std::endl;
    return 0;
}
