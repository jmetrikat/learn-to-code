/**
 * Recursive C program to calculate the least common multiple of two given numbers.
 *
 * @File = lcm.c
 * @Date = 2023-03-29
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <stdio.h>
#include <stdlib.h>

/* calculate greatest common divisor using euclid's algorithm */
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }

    return gcd(b, a % b);
}

/* calculate least common multiple using greatest common divisor */
int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <number1> <number2>\n", argv[0]);
        return 1;
    }

    printf("%d\n", lcm(atoi(argv[1]), atoi(argv[2])));
    return 0;
}
