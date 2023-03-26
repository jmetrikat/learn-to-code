/**
 * C programm to calculate all prime numbers up to a given number.
 *
 * @File = primes.c
 * @Date = 2023-03-26
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <stdio.h>
#include <stdlib.h>

/* calculate primes using the sieve of eratosthenes */
void primes(int n) {
    int *is_prime = (int *) malloc((n + 1) * sizeof(int));

    for (int i = 0; i <= n; i++) {
        is_prime[i] = 1;
    }

    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i] == 1) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    for (int i = 2; i <= n; i++) {
        if (is_prime[i] == 1) {
            printf("%d\n", i);
        }
    }

    free(is_prime);
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

    primes(n);
    return 0;
}
