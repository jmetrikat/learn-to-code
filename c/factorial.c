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

/**
 * Calculates the factorial of a given number.
 */
int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

/**
 * main function.
 */
int main(int argc, char *argv[]) {
    int n;

    if (argc != 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return -1;
    }

    n = atoi(argv[1]);
    printf("%d\n", factorial(n));
    return 0;
}
