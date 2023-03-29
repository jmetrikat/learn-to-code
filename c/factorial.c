/**
 * Recursive C programm to calculate the factorial of a given number.
 *
 * @File = factorial.c
 * @Date = 2022-12-28
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <stdio.h>
#include <stdlib.h>

/* calculates the factorial of a given number */
long long factorial(long long n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

/* main function */
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    if (n < 0) {
        fprintf(stderr, "Number must be positive.\n");
        return 1;
    }

    printf("%lld\n", factorial(n));
    return 0;
}
