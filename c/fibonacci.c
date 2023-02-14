/**
 *  C programm utilizing memoization to calculate the fibonacci number of a given number.
 *
 * @File = fibonacci.c
 * @Date = 2022-12-29
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <stdio.h>
#include <stdlib.h>

/* calculate fibonacci number of a given number */
long long fibonacci(long long n) {
    long long *fib = (long long *) malloc((n + 1) * sizeof(long long));

    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    long long result = fib[n];
    free(fib);

    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number>\n", argv[0]);
        return 1;
    }

    printf("%lld\n", fibonacci(atoi(argv[1])));
}
