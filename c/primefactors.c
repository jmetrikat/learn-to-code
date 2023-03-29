/**
 * C program to calculate prime factors of a given number.
 *
 * @File = primefactors.c
 * @Date = 2023-03-26
 * @Author = Jannis Metrikat
 * @Version = Version 1.0
 */

#include <stdio.h>
#include <stdlib.h>

/* calculate prime factors of a given number */
void primefactors(int n) {
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
            printf("%d\n", i);
            found_factor = 1;
        }
    }

    if (!found_factor) {
        printf("%d is prime.\n", n);
    }

    return;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    if (n < 2) {
        fprintf(stderr, "Number must be greater than 1.\n");
        return 1;
    }

    primefactors(n);
    return 0;
}
